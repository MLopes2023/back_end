from datetime                       import datetime
from pydantic                       import BaseModel
from typing                         import List
from model.participante             import Participante

class ParticipanteFormSchema(BaseModel):
    """ Representação da forma que um novo participante da lista restritiva será inserido.
    """
    nome_participante: str = "MARCOS MALAFAIA"
    id_class_participante:int = 1 
    id_pais_doc_participante: int = 1
    id_doc_participante:int = 1
    num_doc_participante: str = "99999999999"
    
class ParticipanteFormEditarSchema(BaseModel):
    """ Representação da forma que um participante da lista restritiva será editado.
    """
    id_participante:int = 1
    nome_participante: str = "MARCOS MALAFAIA"
    id_class_participante:int = 1 
    id_pais_doc_participante: int = 1
    id_doc_participante:int = 1
    num_doc_participante: str = "99999999999"
    
class ParticipanteVisualizaSchema(BaseModel):
    """ Representação da forma que um participante da lista restritiva será retornado.
    """
    id_participante_ident:int = 1
    nome_participante: str = "MARCOS MALAFAIA"
    id_class_participante:int = 1 
    id_pais_doc_participante: int = 1
    id_doc_participante:int = 1
    num_doc_participante: str = "99999999999"
    data_cadastro_participante:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_participante:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    classificacao: str = "PESSOA FISICA NACIONAL"
    pais_documento: str = "BRASIL"
    documento: str = "CPF"

class ParticipanteBuscaSchema(BaseModel):
    """ Representação da estrutura para busca participante(s) da lista restritiva ou que possam satisfazer os filtros opcionais informados.
    """
    documento_participante: str = "CPF"
    num_doc_participante: str = ""

class ParticipanteIdBuscaSchema(BaseModel):
    """ Representação da estrutura para busca de um determinado participante da lista restritiva conforme id informado.
    """
    id_participante: int = 1

class ParticipanteDeleteSchema(BaseModel):
    """ Representação da estrutura do dado retornado após uma requisição de exclusão de um participante da lista restritiva.
    """
    mensagem: str

class ListaParticipante(BaseModel):
    """ Define uma lista de participantes da lista restritiva que deverão ser retornados.
    """
    participantes:List[ParticipanteVisualizaSchema]


def apresenta_participante(participante: Participante):
    """ Retorna uma representação de um participante da lista restritiva, seguindo o schema definido em ParticipanteVisualizaSchema.
    """
    return {
       "id_participante": participante.Participante.id_participante,
       "nome_participante": participante.Participante.nome_participante,
       "id_class_participante": participante.Participante.id_class_participante,
       "id_pais_doc_participante": participante.Participante.id_pais_doc_participante,
       "id_doc_participante": participante.Participante.id_doc_participante,
       "num_doc_participante": participante.Participante.num_doc_participante,
       "classificacao": participante.Classificacao.descricao_class,
       "pais_documento": participante.Pais.nome_pais,
       "documento": participante.Documento.documento,
       "data_cadastro_participante": participante.Participante.data_cadastro_participante.strftime("%Y-%m-%d %H:%M:%S"),
       "data_alteracao_participante": participante.Participante.data_alteracao_participante.strftime("%Y-%m-%d %H:%M:%S"),
    }

def apresenta_lista_participantes(participantes: List[Participante]):
    """ Retorna uma representação da lista de participantes da lista restritiva, seguindo o schema definido em ParticipanteVisualizaSchema.
    """
    result = []
    for participante in participantes:
        result.append({
             "id_participante": participante.Participante.id_participante,
            "nome_participante": participante.Participante.nome_participante,
            "id_class_participante": participante.Participante.id_class_participante,
            "id_pais_doc_participante": participante.Participante.id_pais_doc_participante,
            "id_doc_participante": participante.Participante.id_doc_participante,
            "num_doc_participante": participante.Participante.num_doc_participante,
            "classificacao": participante.Classificacao.descricao_class,
            "pais_documento": participante.Pais.nome_pais,
            "documento": participante.Documento.documento,
            "data_cadastro_participante": participante.Participante.data_cadastro_participante.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_participante": participante.Participante.data_alteracao_participante.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return {"participantes": result}
