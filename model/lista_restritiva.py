from sqlalchemy     import Column, String, DateTime
from datetime       import datetime
from typing         import Union
from model.base     import Base

#Tabela de identificação da lista restritiva 
class Lista_Restritiva(Base):
    __tablename__ = 'lista_restritiva'

    ident_lista             = Column(String(15), primary_key=True)
    descricao_lista         = Column(String(50), unique=True)
    data_cadastro_lista     = Column(DateTime,   default=datetime.now())
    data_alteracao_lista    = Column(DateTime,   default=datetime.now())
    
    #construtor
    def __init__(self,ident_lista:str, descricao_lista:str, data_cadastro_lista:Union[DateTime, None] = None, data_alteracao_lista:Union[DateTime, None] = None  ):
        """
        Cria identificação da lista restritiva

        Arguments:
            ident_lista: Código de identificação da lista restritiva.
            descricao_lista: Descrição de identificação da lista restritiva.
            data_cadastro_lista: Data/hora do cadastro do identificador da lista restritiva.
            data_alteracao_lista: Data/hora da alteração do identificador da lista restritiva.
        """
        self.ident_lista   = ident_lista
        self.descricao_lista = descricao_lista.upper()
        
        if not data_cadastro_lista:
            self.data_cadastro_lista = datetime.now()
        else:
            self.data_cadastro_lista = data_cadastro_lista
  
        if not data_alteracao_lista:
            self.data_alteracao_lista = datetime.now()
        else:
            self.data_alteracao_lista = data_alteracao_lista
    