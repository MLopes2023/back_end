from sqlalchemy import Column, String, Integer, DateTime
from datetime   import datetime
from typing     import Union

from  model.base import Base

#Tabela de documentos ( CPF, CNPJ, PASSAPORTE)
class Documento(Base):
    __tablename__ = 'documento'

    id_documento                = Column(Integer,    primary_key=True, default=0 )
    documento                   = Column(String(50), unique=True)
    descricao_documento         = Column(String(40), nullable=False)
    perfil_documento            = Column(String(1),  nullable=False)
    data_cadastro_documento     = Column(DateTime,   default=datetime.now(),     nullable=False)
    data_alteracao_documento    = Column(DateTime,   default=datetime.now(),     nullable=False)
    
    #construtor
    def __init__(self,id_documento:int, documento:str, descricao_documento:str, perfil_documento:str, data_cadastro_documento:Union[DateTime, None] = None, data_alteracao_documento:Union[DateTime, None] = None  ):
        """
        Cria documentos

        Arguments:
            id_documento: Id do documento.
            documento: Nome do documento.
            descricao_documento: Descrição do documento.
            data_cadastro_documento: Data/hora do cadastro do documento.
            data_alteracao_documento: Data/hora da alteração do documento.
        """
        self.id_documento           = id_documento
        self.documento              = documento.upper()
        self.descricao_documento    = descricao_documento
        self.perfil_documento       = perfil_documento
        
        if not data_cadastro_documento:
            self.data_cadastro_documento = datetime.now()
        else:
            self.data_cadastro_documento = data_cadastro_documento
  
        if not data_alteracao_documento:
            self.data_alteracao_documento = datetime.now()
        else:
            self.data_alteracao_documento = data_alteracao_documento
    