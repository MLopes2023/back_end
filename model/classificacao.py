from sqlalchemy     import Column, String, Integer, DateTime
from datetime       import datetime
from typing         import Union
from  model.base    import Base

#Tabela de classificação do participante (pessoa física nacional, Pessoa jurídica nacional)
class Classificacao(Base):
    __tablename__ = 'classificacao'

    id_class              = Column(Integer,     primary_key=True, default=0 )
    descricao_class       = Column(String(30),  unique=True)
    perfil_class          = Column(String(1),   nullable=False)
    flag_nacional_class   = Column(String(1),   nullable=False)
    flag_favorito_class   = Column(String(1),   nullable=False)
    data_cadastro_class   = Column(DateTime,    default=datetime.now(),     nullable=False)
    data_alteracao_class  = Column(DateTime,    default=datetime.now(),     nullable=False)
    
    #construtor
    def __init__(self,id_class:int, descricao_class:str, perfil_class:str, flag_nacional_class:str, flag_favorito_class:str,  data_cadastro_class:Union[DateTime, None] = None, data_alteracao_class:Union[DateTime, None] = None  ):
        """
        Cria classificação do participante

        Arguments:
            id_class: Id da classificação do participante.
            descricao_class: Descrição da classificação do participante.
            perfil_class: Perfil da classificação do participante "F" = Pessoa física nacional ou "J" = Pessoa jurídica nacional.
            flag_nacional_class: Flag de identificação de classificação de pessoa física e jurídica nacioal "S" ou "N" = estrangeira.
            flag_favorito_class: Flag de identificação classificação favorita por perfil "S" = favorita ou "N" = não favorita.
            data_cadastro_class: Data/hora do cadastro da classificação.
            data_alteracao_class: Data/hora da alteração da classificação.
        """
        self.id_class               = id_class
        self.descricao_class        = descricao_class
        self.perfil_class           = perfil_class
        self.flag_nacional_class    = flag_nacional_class
        self.flag_favorito_class    = flag_favorito_class
        
        if not data_cadastro_class:
            self.data_cadastro_class = datetime.now()
        else:
            self.data_cadastro_class = data_cadastro_class
  
        if not data_alteracao_class:
            self.data_alteracao_class = datetime.now()
        else:
            self.data_alteracao_class = data_alteracao_class
    