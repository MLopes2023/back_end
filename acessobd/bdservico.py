from datetime       import datetime
from operator       import and_, or_
from model          import Classificacao, Documento, Lista_Restritiva, Pais, Participante, Pesquisa, Status_Lista
from acessobd.bd    import *

###############################################################################
# Classe de manuseio banco de dados.
###############################################################################

class BdServico(Bd):

    ###########################################################################
    # Inicializa o contrutor da classe BdServico e Bd.
    ###########################################################################
    
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()
    
    ###########################################################################
    #  Implementando métodos das classe abstrata ( Contrato ).
    ###########################################################################

    @property
    def operacao_alterar(self):
        return super().operacao_alterar

    @property
    def operacao_excluir(self):
        return super().operacao_excluir

    @property
    def operacao_incluir(self):
        return super().operacao_incluir
    
    def is_operacao_alteacao(self, operacao):
        return super().is_operacao_alteacao(operacao)
    
    def is_operacao_exclusao(self, operacao):
        return super().is_operacao_exclusao(operacao)
    
    def is_operacao_inclusao(self, operacao):
        return super().is_operacao_inclusao(operacao)

    @property
    def session(self):
        return super().session
    
    def get_formata_data_filter(self, datafilter:datetime  ):
        return super().get_formata_data_filter(datafilter )

    def get_formata_data_hora_filter(self, datafilter:datetime  ):
        return super().get_formata_data_hora_filter(datafilter)
    
    def get_select_all(self, tabela):
        return  super().get_select_all(tabela)
    
    def get_select_first(self, tabela, filtro):
        return super().get_select_first(tabela, filtro)
    
    def get_select_max_number(self, colmax):
        return super().get_select_max_number(colmax)
    
    def add_tabela(self, tabela, autocommit=True):
        super().add_tabela(tabela, autocommit)     
    
    def update_tabela(self, tabela, filtro, values, autocommit=True):
        super().update_tabela(tabela, filtro, values, autocommit)
        
    def del_tabela(self, tabela, filtro, value, autocommit=True):
        return super().del_tabela(tabela, filtro, value, autocommit)
    
    def commit_sessao(self):
        super().commit_sessao()
   
    def rollback_sessao(self):
        super().rollback_sessao()
 
    ###########################################################################
    #  Implementando métodos relacionaos ao país do documeto do participante.
    ###########################################################################
            
    # Função para verificar existência do país na base de dados
    def get_id_pais_existe(self, id_value:int):
        
        existe = False
        filtro = Pais.id_pais == id_value
        obj    = self.get_select_first(Pais,  filtro)
        
        if obj:
            existe = True
        
        return  existe
         
    # Função para retornar um único ou todos os países cadastrados na base de dados.
    def get_objeto_paises(self, id_value:int=0):
        if id_value == 0 or id_value == None:
            obj = self.get_select_all(Pais)
        else:     
            filtro = Pais.id_pais == id_value
            obj    = self.get_select_first(Pais,  filtro)
        return obj    
    
    ###########################################################################
    #  Implementando método relacionao a classificação do participante.
    ###########################################################################

    # Função para verificar existência da classificação na base de dados
    def get_id_classificacao_existe(self, id_value:int):
        
        existe = False
        filtro = Classificacao.id_class == id_value
        obj    = self.get_select_first(Classificacao,  filtro)
        
        if obj:
            existe = True
        
        return  existe

    # Função para retornar uma única ou todas as classificacoes do participante cadastradas na base de dados.
    def get_objeto_classificacoes(self, id_value:int):
        if id_value == 0 or id_value == None:
            obj =  self.get_select_all(Classificacao)    
        else:
            filtro = Classificacao.id_class == id_value
            obj    = self.get_select_first(Classificacao,  filtro)
        return obj
    
    ###########################################################################
    #  Implementando método relacionao ao documento do participante
    ###########################################################################
   
    # Função para verificar existência da classificação na base de dados.
    def get_id_documento_existe(self, id_value:int):
        
        existe = False
        filtro = Documento.id_documento == id_value
        obj    = self.get_select_first(Documento,  filtro)
        
        if obj:
            existe = True
        
        return  existe

    # Função para retornar um único ou todos documentos cadastrados na base de dados, conforme filtro.
    def get_objeto_documentos(self, id_value:int=0, documento_value:str=""):
        
        
        if ((id_value == 0 or id_value == None) and (documento_value == "" or documento_value == None)):
            obj =  self.get_select_all(Documento)
        else:
            if (id_value != 0 and id_value != None):
                filtro = Documento.id_documento == id_value
            elif (documento_value != "" and documento_value != None):
                filtro = Documento.documento == documento_value    
            else:    
                filtro = Documento.id_documento == id_value
            obj    = self.get_select_first(Documento,  filtro)   
        return obj
    
    ###########################################################################
    #  Implementando métodos relacionaos ao participante da lista restritiva
    ###########################################################################
   
   # Função para retornar o objeto com os dados de um participante conforme id informado.
    def get_objeto_participante_Filtro_id(self, value:int):
        return  self.get_select_first(Participante, Participante.id_participante == value)
 
    # Função para retornar o incremento id do participante da lista restritiva.
    def get_id_participante_novo(self):
        idnovo = self.get_select_max_number(Participante.id_participante) + 1
        return idnovo

    # Função para verificar se o documento do participante já existe no base de dados.
    # Pode ser executada informando todos os filtros ou apenas pelo num_doc_participante.
    def get_documento_participante_existe(self, id_pais_doc_participante:int=0, id_doc_participante:str="", num_doc_participante:str="", id_participante_value:int=0):
        
        existe = False
        
        if id_pais_doc_participante != 0 and id_pais_doc_participante != None and id_doc_participante != "" and id_doc_participante != None and id_participante_value != 0 and id_participante_value != None:
            obj    = self.session.query(Participante).\
                                filter(Participante.id_participante != id_participante_value,\
                                        Participante.id_pais_doc_participante == id_pais_doc_participante,\
                                        Participante.id_doc_participante  == id_doc_participante,\
                                        Participante.num_doc_participante == num_doc_participante).first()
        else:
            obj    = self.session.query(Participante).\
                                filter( Participante.num_doc_participante == num_doc_participante).first()
        if obj:
            existe = True
        
        return  existe

    # Função para retornar um único participante da lista restritiva cadastrado na base de dados.
    # Filtrar pelo id do participante ou pelo país, documento e numero do documento do participante.
    def get_objeto_participante(self, id_participante:int, id_pais_doc_participante:int=0, documento_participante:str="", num_doc_participante:str=""  ):
        
        if id_pais_doc_participante != 0 and id_pais_doc_participante != None and documento_participante != "" and documento_participante != None and num_doc_participante != "" and num_doc_participante != None:
            participante  =  self.session.query(Participante, Classificacao, Documento, Pais).\
                                          filter(Pais.id_pais        == id_pais_doc_participante,\
                                                 Documento.documento == documento_participante,
                                                 Participante.num_doc_participante == num_doc_participante).\
                                           filter(Classificacao.id_class==Participante.id_class_participante,\
                                                  Documento.id_documento==Participante.id_doc_participante,\
                                                  Pais.id_pais==Participante.id_pais_doc_participante).first()
        else:
            participante  =  self.session.query(Participante, Classificacao, Documento, Pais).\
                                        filter(Participante.id_participante==id_participante).\
                                        filter(Classificacao.id_class==Participante.id_class_participante,\
                                                Documento.id_documento==Participante.id_doc_participante,\
                                                Pais.id_pais==Participante.id_pais_doc_participante).first()

        return  participante 

    # Função para retornar todos os participante da lista restritiva cadastradas na base de dados.
    def get_objeto_participantes(self, documento_participante:str="", num_doc_participante:str=""):
        
        if ((documento_participante == "" or documento_participante == None) and (num_doc_participante == "" or num_doc_participante == None)):
            participantes =  self.session.query(Participante, Classificacao, Documento, Pais).\
                                        filter(Classificacao.id_class==Participante.id_class_participante,\
                                                Documento.id_documento==Participante.id_doc_participante,\
                                                Pais.id_pais==Participante.id_pais_doc_participante).all()
        elif ((documento_participante != "" and documento_participante != None) and (num_doc_participante != "" and num_doc_participante != None)):                                        
            participantes =  self.session.query(Participante, Classificacao, Documento, Pais).\
                                          filter(Documento.documento                    ==documento_participante).\
                                          filter(Participante.num_doc_participante      ==num_doc_participante).\
                                          filter(Classificacao.id_class                 ==Participante.id_class_participante,\
                                                Documento.id_documento                  ==Participante.id_doc_participante,\
                                                Pais.id_pais                            ==Participante.id_pais_doc_participante).all()
        elif documento_participante != "" and documento_participante != None:                                        
            participantes =  self.session.query(Participante, Classificacao, Documento, Pais).\
                                          filter(Documento.documento                    ==documento_participante).\
                                          filter(Classificacao.id_class                 ==Participante.id_class_participante,\
                                                Documento.id_documento                  ==Participante.id_doc_participante,\
                                                Pais.id_pais                            ==Participante.id_pais_doc_participante).all()
        elif num_doc_participante != "" and num_doc_participante != None:                                        
            participantes =  self.session.query(Participante, Classificacao, Documento, Pais).\
                                          filter(Participante.num_doc_participante      ==num_doc_participante).\
                                          filter(Classificacao.id_class                 ==Participante.id_class_participante,\
                                                Documento.id_documento                  ==Participante.id_doc_participante,\
                                                Pais.id_pais                            ==Participante.id_pais_doc_participante).all()
        return  participantes
    
    # Método para adicionar um novo participante da lista restritiva na base de dados.
    def add_participante(self, tabela:Participante, autocommit=True):
        self.add_tabela(tabela, autocommit)
        
    # Método para editar um participante da lista restritiva na base de dados.
    def update_participante(self, id_participante:int, nome_participante:str, id_class_participante:int, id_pais_doc_participante, id_doc_participante:int, num_doc_participante:str, autocommit=True):

        filtro = Participante.id_participante == id_participante
        values = {Participante.nome_participante: nome_participante, Participante.id_class_participante:id_class_participante,\
                  Participante.id_pais_doc_participante:id_pais_doc_participante, Participante.id_doc_participante:id_doc_participante, Participante.num_doc_participante:num_doc_participante, Participante.data_alteracao_participante: datetime.now()}
        self.update_tabela(Participante, filtro, values, autocommit )        
   
   # Remover participante da lista restritiva da base de dados
    def del_participante(self, value:int, autocommit=True):
        count   = self.del_tabela(Participante, Participante.id_participante == value, value, autocommit)
        return count        

    ###########################################################################
    # Implementando métodos relacionados ao identificador da lista restritiva.
    ###########################################################################
    
    # Função para retornar todos um único ou todos os identificadores da lista 
    # restritiva cadastrados na base de dados.
    
    def get_objeto_identificadores_listas_restritivas(self, id_value:str=None):
        if id_value == "" or id_value == None:
            obj =  self.get_select_all(Lista_Restritiva)
        else:
            filtro = Lista_Restritiva.ident_lista == id_value
            obj    = self.get_select_first(Lista_Restritiva,  filtro)   
        return obj

    ###########################################################################
    #  Implementando métodos relacionaos ao status dos identificadores da lista
    #  restritiva.
    ###########################################################################
    
    # Função para retornar um ou todos os status dos identificadores da lista 
    # restritiva cadastradas na base de dados, com o filtro identificador opcional.
    
    def get_objeto_status_identificadores_listas_restritivas(self, ident_lista_status:str=None):
        
        if ident_lista_status == "" or ident_lista_status == None:
            status_listas =  self.session.query(Status_Lista, Lista_Restritiva).\
                                          filter(Lista_Restritiva.ident_lista==Status_Lista.ident_lista_status).all()
        else:
            status_listas =  self.session.query(Status_Lista, Lista_Restritiva).\
                                          filter( Status_Lista.ident_lista_status == ident_lista_status,\
                                                  Lista_Restritiva.ident_lista==Status_Lista.ident_lista_status).all()
                                                      
        return  status_listas
 
     ###########################################################################
    #  Implementando métodos relacionaos ao cadastro de pesquisa de participantes
    #  da lista restritiva.
    ###########################################################################
    
    # Função para retornar uma única simulação de pesquisa cadastrada na base de dados.
    def get_objeto_pesquisa(self, numero_pesquisa:int):
        
        pesquisa =  self.session.query(Classificacao, Pais, Documento, Participante, Pesquisa, Status_Lista, Lista_Restritiva).\
                                      filter(Pesquisa.numero_pesquisa     == numero_pesquisa).\
                                      filter(Classificacao.id_class       == Participante.id_class_participante,\
                                             Documento.id_documento       == Participante.id_doc_participante,\
                                             Pais.id_pais                 == Participante.id_pais_doc_participante,\
                                             Participante.id_participante == Pesquisa.id_participante_pesquisa,\
                                             Status_Lista.id_status_lista == Pesquisa.id_status_lista_pesquisa,\
                                             Lista_Restritiva.ident_lista == Status_Lista.ident_lista_status).first()                                      
        return  pesquisa

    # Função para retornar a lista das pesquisas entre datas cadastradas e que
    #  também possam satisfazer outros filtros opcionais da consulta.
    def get_objeto_pesquisa_participantes_listas_restritivas(self, data_pesquisa_inicial:datetime,  data_pesquisa_final:datetime,
                                                                   documento_participante:str="",   num_doc_participante:str="" ):
        
        # Define filtro das datas
        filtro_datas = Pesquisa.data_pesquisa.between(self.get_formata_data_hora_filter(data_pesquisa_inicial), self.get_formata_data_hora_filter(data_pesquisa_final))   

        # Executar query conforme filtro    
        if ((documento_participante == "" or documento_participante == None) and (num_doc_participante == "" or num_doc_participante == None)):
            pesquisas =  self.session.query(Classificacao, Pais, Documento, Participante, Pesquisa, Status_Lista, Lista_Restritiva).\
                                      filter(filtro_datas).\
                                      filter(Classificacao.id_class       == Participante.id_class_participante,\
                                             Documento.id_documento       == Participante.id_doc_participante,\
                                             Pais.id_pais                 == Participante.id_pais_doc_participante,\
                                             Participante.id_participante == Pesquisa.id_participante_pesquisa,\
                                             Status_Lista.id_status_lista == Pesquisa.id_status_lista_pesquisa,\
                                             Lista_Restritiva.ident_lista == Status_Lista.ident_lista_status).all()
        elif ((documento_participante != "" and documento_participante != None) and (num_doc_participante != "" and num_doc_participante != None)):
            pesquisas =  self.session.query(Classificacao, Pais, Documento, Participante, Pesquisa, Status_Lista, Lista_Restritiva).\
                                      filter(filtro_datas).\
                                      filter(Documento.documento               == documento_participante).\
                                      filter(Participante.num_doc_participante == num_doc_participante).\
                                      filter(Classificacao.id_class       == Participante.id_class_participante,\
                                             Documento.id_documento       == Participante.id_doc_participante,\
                                             Pais.id_pais                 == Participante.id_pais_doc_participante,\
                                             Participante.id_participante == Pesquisa.id_participante_pesquisa,\
                                             Status_Lista.id_status_lista == Pesquisa.id_status_lista_pesquisa,\
                                             Lista_Restritiva.ident_lista == Status_Lista.ident_lista_status).all()
        elif (documento_participante != "" and documento_participante != None):
            pesquisas =  self.session.query(Classificacao, Pais, Documento, Participante, Pesquisa, Status_Lista, Lista_Restritiva).\
                                      filter(filtro_datas).\
                                      filter(Documento.documento          == documento_participante).\
                                      filter(Classificacao.id_class       == Participante.id_class_participante,\
                                             Documento.id_documento       == Participante.id_doc_participante,\
                                             Pais.id_pais                 == Participante.id_pais_doc_participante,\
                                             Participante.id_participante == Pesquisa.id_participante_pesquisa,\
                                             Status_Lista.id_status_lista == Pesquisa.id_status_lista_pesquisa,\
                                             Lista_Restritiva.ident_lista == Status_Lista.ident_lista_status).all()
        elif (num_doc_participante != "" and num_doc_participante != None):
            pesquisas =  self.session.query(Classificacao, Pais, Documento, Participante, Pesquisa, Status_Lista, Lista_Restritiva).\
                                      filter(filtro_datas).\
                                      filter(Participante.num_doc_participante == num_doc_participante).\
                                      filter(Classificacao.id_class       == Participante.id_class_participante,\
                                             Documento.id_documento       == Participante.id_doc_participante,\
                                             Pais.id_pais                 == Participante.id_pais_doc_participante,\
                                             Participante.id_participante == Pesquisa.id_participante_pesquisa,\
                                             Status_Lista.id_status_lista == Pesquisa.id_status_lista_pesquisa,\
                                             Lista_Restritiva.ident_lista == Status_Lista.ident_lista_status).all()
        return  pesquisas
 
    # Função para retornar o incremento numero da pesquisa da lista restritiva.
    def get_numero_pesquisa_novo(self):
        idnovo = self.get_select_max_number(Pesquisa.numero_pesquisa) + 1
        return idnovo

    # Método para adicionar um nova pesquisa do participante da lista restritiva na base de dados.
    def add_pesquisa(self, tabela:Pesquisa, autocommit=True):
        self.add_tabela(tabela, autocommit)
