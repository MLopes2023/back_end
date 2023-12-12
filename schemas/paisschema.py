from datetime   import datetime
from pydantic   import BaseModel
from typing     import List
from model.pais import Pais

class PaisVisualizaSchema(BaseModel):
    """ Representação da forma que um país será retornado.
    """
    id_pais:   int = 1 
    nome_pais: str = "BRASIL"
    flag_pais_nacional:str = "S"
    data_cadastro_pais:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_pais:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ListaPaisSchema(BaseModel):
    """ Define uma lista de países que deverão ser retornados.
    """
    paises:List[PaisVisualizaSchema]

def apresenta_lista_paises(paises: List[Pais]):
    """ Retorna uma representação da lista de países, seguindo o schema definido em PaisVisualizaSchema.
    """
    result = []
    for pais in paises:
        result.append({
            "id_pais": pais.id_pais,   
            "nome_pais": pais.nome_pais,
            "flag_pais_nacional": pais.flag_pais_nacional,
            "data_cadastro_pais": pais.data_cadastro_pais.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_pais": pais.data_alteracao_pais.strftime("%Y-%m-%d %H:%M:%S")
        })

    return {"paises": result}
