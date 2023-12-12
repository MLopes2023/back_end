from datetime               import datetime
from pydantic               import BaseModel
from typing                 import List
from model.status_lista     import Status_Lista

class StatusListaVisualizaSchema(BaseModel):
    """ Representação da forma que um status do identificador da lista restritiva será retornado.
    """
    id_status_lista:int = 1
    ident_lista_status: str = "LISTA-SRF"
    codigo_status:int = 1      
    descricao_status: str = "REGULAR"
    descricao_lista: str = "SRF-SECRETARIA RECEITA FEDERAL"
    data_cadastro_status:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_status:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class StatusListaIdBuscaSchema(BaseModel):
    """ Representação da estrutura para busca de um determinado status do identificador da lista restritiva ou todos, se id da identificação não for informado.
    """
    ident_lista_status: str = "LISTA-SRF"
    
class ListaStatusSchema(BaseModel):
    """ Define uma lista dos status dos identificadores da lista restritiva que deverão ser retornados.
    """
    status_listas:List[StatusListaVisualizaSchema]

def apresenta_lista_status_identificadores_lista_restritiva(status_listas: List[ListaStatusSchema]):
    """ Retorna uma representação da lista dos status dos identificadores da lista restritiva, seguindo o schema definido em StatusListaVisualizaSchema.
    """
    result = []
    for status_lista in status_listas:
        result.append({
            "id_status_lista": status_lista.Status_Lista.id_status_lista,
            "ident_lista_status": status_lista.Status_Lista.ident_lista_status,
            "codigo_status": status_lista.Status_Lista.codigo_status,
            "descricao_status": status_lista.Status_Lista.descricao_status,
            "descricao_lista": status_lista.Lista_Restritiva.descricao_lista,
            "data_cadastro_participante": status_lista.Status_Lista.data_cadastro_status.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_participante": status_lista.Status_Lista.data_alteracao_status.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return {"status_listas": result}
