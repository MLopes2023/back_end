from datetime               import datetime
from pydantic               import BaseModel
from typing                 import List
from model.lista_restritiva import Lista_Restritiva

class ListaRestritivaVisualizaSchema(BaseModel):
    """ Representação da forma que um identificador da lista restritiva será retornado.
    """
    ident_lista: str = "LISTA-SRF"
    descricao_lista: str = "SRF-SECRETARIA RECEITA FEDERAL"
    data_cadastro_lista:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_lista:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ListaRestritivaSchema(BaseModel):
    """ Define uma lista de identificadores da lista restritiva que deverão ser retornados.
    """
    listas_restritivas:List[ListaRestritivaVisualizaSchema]

def apresenta_lista_da_lista_restritiva(listas_restritivas: List[Lista_Restritiva]):
    """ Retorna uma representação da lista de identificadores da lista restritiva, seguindo o schema definido em ListaRestritivaVisualizaSchema.
    """
    result = []
    for listas_restritiva in listas_restritivas:
        result.append({
            "ident_lista": listas_restritiva.ident_lista,   
            "descricao_lista": listas_restritiva.descricao_lista,
            "data_cadastro_lista": listas_restritiva.data_cadastro_lista.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_lista": listas_restritiva.data_alteracao_lista.strftime("%Y-%m-%d %H:%M:%S")
        })

    return {"listas_restritivas": result}
