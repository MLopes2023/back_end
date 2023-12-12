from sqlalchemy             import Column, String, Integer, DateTime, ForeignKey, Index
from datetime               import datetime
from typing                 import Union
from  model.base            import Base

#Tabela de participantes da lista restritiva
class Participante(Base):
    __tablename__ = 'participante'

    id_participante             = Column(Integer,       primary_key=True, default=0 )
    nome_participante           = Column(String(100),   nullable=False)
    id_class_participante       = Column(Integer,       ForeignKey("classificacao.id_class"),  nullable=False)
    id_pais_doc_participante    = Column(Integer,       ForeignKey("pais.id_pais"),            nullable=False)
    id_doc_participante         = Column(Integer,       ForeignKey("documento.id_documento"),  nullable=False)
    num_doc_participante        = Column(String(25),    nullable=False)
    data_cadastro_participante  = Column(DateTime,      default=datetime.now(),     nullable=False)
    data_alteracao_participante = Column(DateTime,      default=datetime.now(),     nullable=False)
    
    # Define chave única
    __table_args__ = (
        Index(id_pais_doc_participante, id_doc_participante, num_doc_participante, unique=True),
        {},
    )
    
    #construtor
    def __init__(self,id_participante:int, nome_participante:str, id_class_participante:int, id_pais_doc_participante:int, id_doc_participante:int, num_doc_participante:str,  data_cadastro_participante:Union[DateTime, None] = None, data_alteracao_participante:Union[DateTime, None] = None  ):
        """
        Cria participante da lista restritiva

        Arguments:
            id_participante: Id do participante.
            nome_participante: Nome do participante.
            id_class_participante: id da classificação do participante.
            id_pais_doc_participante: Id do país do documento do participante: ( 1 = BRASIL).
            id_doc_participante: Id do documento do participante: ( 1 = CPF OU 2 = "CNPJ ).
            num_doc_participante: Número do documento de identificação do participante.
            data_cadastro_participante: Data/hora do cadastro do participante.
            data_alteracao_participante: Data/hora da alteração do cadastro do participante.
        """
        self.id_participante            = id_participante
        self.nome_participante          = nome_participante
        self.id_class_participante      = id_class_participante
        self.id_pais_doc_participante   = id_pais_doc_participante
        self.id_doc_participante        = id_doc_participante
        self.num_doc_participante       = num_doc_participante
        
        if not data_cadastro_participante:
            self.data_cadastro_participante = datetime.now()
        else:
            self.data_cadastro_participante = data_cadastro_participante
  
        if not data_alteracao_participante:
            self.data_alteracao_participante = datetime.now()
        else:
            self.data_alteracao_participante = data_alteracao_participante
