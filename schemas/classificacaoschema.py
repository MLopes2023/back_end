from datetime import datetime
from pydantic               import BaseModel
from typing                 import List
from model.classificacao    import Classificacao
  
class ClassificacaoVisualizaSchema(BaseModel):
    """ Representação da forma que uma classificação será retornada.
    """
    id_class:   int = 1 
    descricao_class: str = "PESSOA FÍSICA"
    perfil_class:str = "F"
    flag_nacional_class:str = "S"
    flag_favorito_class:str = "S"
    data_cadastro_class:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_class:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ListaClassificacaoSchema(BaseModel):
    """ Define uma lista de classificações que deverão ser retornadas.
    """
    documentos:List[ClassificacaoVisualizaSchema]


def apresenta_lista_classificacoes(classificacoes: List[Classificacao]):
    """ Retorna uma representação da lista de classificações, seguindo o schema definido em ClassificacaoVisualizaSchema.
    """
    result = []
    for classificacao in classificacoes:
        result.append({
            "id_class": classificacao.id_class,   
            "descricao_class": classificacao.descricao_class,
            "perfil_class": classificacao.perfil_class,
            "flag_nacional_class": classificacao.flag_nacional_class,
            "flag_favorito_class": classificacao.flag_favorito_class,
            "data_cadastro_class": classificacao.data_cadastro_class.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_class": classificacao.data_alteracao_class.strftime("%Y-%m-%d %H:%M:%S")
        })

    return {"classificacoes": result}
