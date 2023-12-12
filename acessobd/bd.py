import abc
import functools
from datetime           import datetime, timedelta 
#from sqlalchemy.exc     import IntegrityError
from sqlalchemy         import func
#from sqlalchemy         import update
#from pydantic           import BaseModel
#from typing             import Optional, List
from model              import Session
from acessobd.bdoperacao import BdOperacao

# Classe reponsável pelo acesso ao banco de dados
class Bd(abc.ABC):

    def __init__(self):
        
        # Cria objeto da classe de identificação do tipo de operação no banco de dados
        self.__bdoperacao = BdOperacao()
        
        # Cria conexão com a base de dados no construtor da classe
        self.__session  = Session()    

    def __del__(self):
        # Conexão encerrada no destrutor da classe
        if self.__session:
            self.__session.close()
    
    # Propriedades e funções de identificação do tipo de operação no banco de dados
    @abc.abstractproperty
    @abc.abstractmethod
    def operacao_alterar(self):
        return self.__bdoperacao.alterar

    @abc.abstractproperty
    @abc.abstractmethod
    def operacao_excluir(self):
        return self.__bdoperacao.excluir

    @abc.abstractproperty
    @abc.abstractmethod
    def operacao_incluir(self):
        return self.__bdoperacao.incluir
    
    @abc.abstractmethod
    def is_operacao_alteacao(self, operacao):
        return self.__bdoperacao.is_alteracao(operacao)
    
    @abc.abstractmethod
    def is_operacao_exclusao(self, operacao):
        return self.__bdoperacao.is_exclusao(operacao)
    
    @abc.abstractmethod
    def is_operacao_inclusao(self, operacao):
        return self.__bdoperacao.is_inclusao(operacao)
    
    # Propiedade de acesso ao objeto Session
    @abc.abstractproperty
    @abc.abstractmethod
    def session(self):
        return self.__session
    
    # Função para formatar datas no Filter
    @abc.abstractmethod
    def get_formata_data_filter(self, datafilter:datetime  ):
        return datafilter.strftime("%Y-%m-%d") 

    @abc.abstractmethod
    def get_formata_data_hora_filter(self, datafilter:datetime  ):
        return datafilter.strftime('%Y-%m-%d %H:%M:%S') 
    
    # Função de retorno do objeto da seleção de todos os registros de uma tabela
    @abc.abstractmethod
    def get_select_all(self, tabela):
        return  self.__session.query(tabela).all()
    
    # Função de retorno seleção da primeira linha de uma tabaela conforme filtro
    @abc.abstractmethod
    def get_select_first(self, tabela, filtro):
        return self.__session.query(tabela).filter(filtro).first()
    
    # Função de retorno maior valor numérico de uma tabela
    @abc.abstractmethod
    def get_select_max_number(self, colmax):
        valormax  = 0
        resultmax = self.__session.query(func.max(colmax)).first()
        if  resultmax is not None and resultmax != (None,):
            valormax = resultmax[0]
        else:
            valormax = 0 
            
        return valormax
    
    # Método para adcionar registro em uma tabela na base de dados
    @abc.abstractmethod
    def add_tabela(self, tabela, autocommit=True):
        
        try:
            self.__session.add(tabela)
        except:
            if autocommit == True:
                self.rollback_sessao()
                raise
        else:
            if autocommit == True:
                self.commit_sessao()        

    # Função para editar registros de uma tabela da base de dados 
    @abc.abstractmethod
    def update_tabela(self, tabela, filtro, values, autocommit=True):
    
        try:
            self.__session.query(tabela).filter(filtro).update(values, synchronize_session =False)
        except:
            if autocommit == True:
                self.rollback_sessao()
                raise
        else:
            if autocommit == True:
                self.commit_sessao()        
            
    # Função para remover linha(s) de uma tabela da base de dados conforme único indice de uma tabela
    @abc.abstractmethod
    def del_tabela(self, tabela, filtro, value, autocommit=True):
    
        try:
            count = self.__session.query(tabela).filter(filtro).delete()
        except:
            if autocommit == True:
                self.rollback_sessao()
                raise
        else:
            if autocommit == True:
                self.commit_sessao()        
            
        # Retorna contador de linhas atingidas
        return count
    
    @abc.abstractmethod
    def commit_sessao(self):
        if self.__session:
            self.__session.commit()
    
    @abc.abstractmethod
    def rollback_sessao(self):
        if self.__session:
            self.__session.rollback()    