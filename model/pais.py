from sqlalchemy     import Column, String, Integer, DateTime
from datetime       import datetime
from typing         import Union
from model.base     import Base

#Tabela de países 
class Pais(Base):
    __tablename__ = 'pais'

    id_pais                 = Column(Integer,    primary_key=True, default=0 )
    nome_pais               = Column(String(50), unique=True)
    flag_pais_nacional      = Column(String(1),  nullable=False)
    data_cadastro_pais      = Column(DateTime,   default=datetime.now(),     nullable=False)
    data_alteracao_pais     = Column(DateTime,   default=datetime.now(),     nullable=False)
    
    #construtor
    def __init__(self,id_pais:int, nome_pais:str, flag_pais_nacional:str, data_cadastro_pais:Union[DateTime, None] = None, data_alteracao_pais:Union[DateTime, None] = None  ):
        """
        Cria país

        Arguments:
            id_pais: Id do país
            nome_pais: Nome do país.
            flag_pais_nacional: Flag pais nacional ( "S" para Brasil ou "N" para Estrangeiro). 
            data_cadastro_pais: Data/hora do cadastro do país.
            data_alteracao_pais: Data/hora da alteração do país.
        """
        self.id_pais   = id_pais
        self.nome_pais = nome_pais.upper()
        self.flag_pais_nacional = flag_pais_nacional.upper()
        
        if not data_cadastro_pais:
            self.data_cadastro_pais = datetime.now()
        else:
            self.data_cadastro_pais = data_cadastro_pais
  
        if not data_alteracao_pais:
            self.data_alteracao_pais = datetime.now()
        else:
            self.data_alteracao_pais = data_alteracao_pais
    