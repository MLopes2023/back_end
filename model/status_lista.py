from sqlalchemy             import Column, String, Integer, DateTime, ForeignKey, Index
from sqlalchemy.orm         import relationship
from datetime               import datetime
from typing                 import Union
from model.base             import Base

#Tabela de status do identificador da lista restritiva
class Status_Lista(Base):
    __tablename__ = 'status_lista'

    id_status_lista         = Column(Integer,       primary_key=True, default=0 )
    ident_lista_status      = Column(String(15),    ForeignKey("lista_restritiva.ident_lista"),     nullable=False)
    codigo_status           = Column(Integer,       nullable=False)
    descricao_status        = Column(String(30),    nullable=False)
    data_cadastro_status    = Column(DateTime,      default=datetime.now(),     nullable=False)
    data_alteracao_status   = Column(DateTime,      default=datetime.now(),     nullable=False)
    
    # Cria índice único das colunas identificador da lista restritiva e código do status do identificador
    #__table_args__ = (Index("status_lista_XAK_Index_01", "ident_lista_status", "codigo_status"), )
    Index("status_lista_XAK_Index_01", ident_lista_status, codigo_status, unique=True)
    
    # Define relacionamento  entre status do identificador da lista restritiva e identificador da lista restritiva
    lista_restritiva = relationship("Lista_Restritiva")
    
    #construtor
    def __init__(self,id_status_lista:int, ident_lista_status:str, codigo_status:int, descricao_status:str,  data_cadastro_status:Union[DateTime, None] = None, data_alteracao_status:Union[DateTime, None] = None  ):
        """
        Cria status do identificador da lista restritiva

        Arguments:
            id_status_lista: Id do status do identificador da lista restritiva.
            ident_lista_status: Código de identificação da lista restritiva.
            codigo_status: Código do status do identificador da lista restritiva.
            descricao_status: Descrição do status.
            data_cadastro_status: Data/hora do cadastro do status do identificador da lista restritiva.
            data_alteracao_status: Data/hora da alteração do cadastro do status do identificador da lista restritiva.
        """
        self.id_status_lista        = id_status_lista
        self.ident_lista_status     = ident_lista_status
        self.codigo_status          = codigo_status
        self.descricao_status       = descricao_status
        
        if not data_cadastro_status:
            self.data_cadastro_status = datetime.now()
        else:
            self.data_cadastro_status = data_cadastro_status
  
        if not data_alteracao_status:
            self.data_alteracao_status = datetime.now()
        else:
            self.data_alteracao_status = data_alteracao_status
