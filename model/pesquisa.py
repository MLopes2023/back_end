from sqlalchemy             import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm         import relationship
from datetime               import datetime
from typing                 import Union
from model.base             import Base

#Tabela de pesquisas das listas restritivas dos participantes
class Pesquisa(Base):
    __tablename__ = 'pesquisa'

    numero_pesquisa             = Column(Integer,       primary_key=True, autoincrement=False,     nullable=False,  default=1)
    data_pesquisa               = Column(DateTime,      nullable=False)
    id_participante_pesquisa    = Column(Integer,       ForeignKey("participante.id_participante"),     nullable=False)
    id_status_lista_pesquisa    = Column(Integer,       ForeignKey("status_lista.id_status_lista"),     nullable=False)
    observacao_pesquisa         = Column(String(255),   nullable=False)
    data_cadastro_pesquisa      = Column(DateTime,      default=datetime.now(),     nullable=False)
    data_alteracao_pesquisa     = Column(DateTime,      default=datetime.now(),     nullable=False)
    
    # Define relacionamento entre a tabela de pesquisas das listas restritivas dos participantes e status do identificador da lista restritiva
    status_lista = relationship("Status_Lista")
    
    #construtor
    def __init__(self,numero_pesquisa:int, data_pesquisa:datetime, id_participante_pesquisa:int, id_status_lista_pesquisa:int, observacao_pesquisa:str,  data_cadastro_pesquisa:Union[DateTime, None] = None, data_alteracao_pesquisa:Union[DateTime, None] = None  ):
        """
        Cria pesquisa da lista restritiva dos participantes

        Arguments:
            numero_pesquisa: Número sequencial de controle da pesquisa.
            data_pesquisa: Data da pesquisa.
            id_participante_pesquisa: Id do participante da lista restritiva.
            id_status_lista_pesquisa: Id do códdigo do status do identificador da lista restritiva.
            observacao_pesquisa: Observação opcional da pesquisa.
            data_cadastro_pesquisa: Data/hora do cadastro da pesquisa.
            data_alteracao_pesquisa: Data/hora da alteração da pesquisa.
        """
        numero_pesquisa                 =   numero_pesquisa
        self.data_pesquisa              =   data_pesquisa
        self.id_participante_pesquisa   =   id_participante_pesquisa
        self.id_status_lista_pesquisa   =   id_status_lista_pesquisa
        self.observacao_pesquisa        =   observacao_pesquisa
        
        if not data_cadastro_pesquisa:
            self.data_cadastro_pesquisa = datetime.now()
        else:
            self.data_cadastro_pesquisa = data_cadastro_pesquisa
  
        if not data_alteracao_pesquisa:
            self.data_alteracao_pesquisa = datetime.now()
        else:
            self.data_alteracao_pesquisa = data_alteracao_pesquisa
