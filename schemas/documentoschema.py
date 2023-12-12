from datetime        import datetime
from pydantic        import BaseModel
from typing          import List
from model.documento import Documento
  
class DocumentoVisualizaSchema(BaseModel):
    """ Representação da forma que um documento será retornado.
    """
    id_documento:   int = 1 
    documento: str = "CPF"
    descricao_documento: str = "CADASTRO PESSOA FÍSICA"
    perfil_documento:str = "F"
    data_cadastro_documento:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_documento:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ListaDocumentoSchema(BaseModel):
    """ Define uma lista de documentos que deverão ser retornados.
    """
    documentos:List[DocumentoVisualizaSchema]


def apresenta_lista_documentos(documentos: List[Documento]):
    """ Retorna uma representação da lista de documentos, seguindo o schema definido em DocumentoVisualizaSchema.
    """
    result = []
    for documento in documentos:
        result.append({
            "id_documento": documento.id_documento,   
            "documento": documento.documento,
            "descricao_documento": documento.descricao_documento,
            "perfil_documento": documento.perfil_documento,
            "data_cadastro_documento": documento.data_cadastro_documento.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_documento": documento.data_alteracao_documento.strftime("%Y-%m-%d %H:%M:%S")
        })

    return {"documentos": result}
