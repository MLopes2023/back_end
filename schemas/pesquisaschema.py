from datetime           import datetime
from pydantic           import BaseModel
from typing             import Optional, List
from model.pesquisa     import Pesquisa

class PesquisaVisualizaSchema(BaseModel):
    """ Representação da forma que uma pesquisa do participante na lista restritiva será retornada.
    """
    numero_pesquisa:int = 1
    data_pesquisa: datetime = datetime.now().strftime("%Y-%m-%d")
    id_participante_pesquisa:int = 1    
    id_status_lista_pesquisa:int = 1      
    observacao_pesquisa: str = "OBSERVAÇÃO"
    data_cadastro_pesquisa:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_alteracao_pesquisa:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ident_lista:str = "LISTA-SRF"
    descricao_lista: str = "SRF-SECRETARIA RECEITA FEDERAL"
    codigo_status:int = 1
    descricao_status:str = "REGULAR"
    nome_participante: str = "MARCOS MALAFAIA"
    descricao_classificacao: str = "PESSOA FISICA NACIONAL"
    id_pais:int = 1
    pais_documento: str = "BRASIL"
    id_documento:int = 1
    documento: str = "CPF"
    num_doc_participante: str = "99999999999"

class PesquisaFormSchema(BaseModel):
    """ Representação da forma que um nova pesquisa do participante na lista restritiva será inserida.
    """
    data_pesquisa: datetime = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    id_pais_documento_participante:int = 1
    documento_participante:str = "CPF"
    num_documento_participante:str = "99999999999"
    id_status_lista_pesquisa:int = 1      
    observacao_pesquisa: str = "OBSERVAÇÃO"
    
class PesquisaBuscaSchema(BaseModel):
    """ Representação da estrutura para busca das pesquisas dos participantes na lista restritiva que possam satisfazer os filtros opcionais da solicitação.
    """
    data_pesquisa_inicial: datetime = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    data_pesquisa_final: datetime   = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    documento_participante: str = "CPF"
    num_doc_participante: str = ""
    
class ListaPesquisaSchema(BaseModel):
    """ Define uma lista das pesquisas dos participantes na lista restritiva que deverão ser retornados.
    """
    pesquisas:List[PesquisaVisualizaSchema]

def apresenta_lista_pesquisa(pesquisa: Pesquisa):
    """ Retorna uma representação de uma pesquisa do participante na lista restritiva, seguindo o schema definido em PesquisaVisualizaSchema.
    """
    return {
       "numero_pesquisa": pesquisa.Pesquisa.numero_pesquisa,
            "data_pesquisa": pesquisa.Pesquisa.data_pesquisa.strftime("%Y-%m-%d"),
            "data_pesquisa_fmt_br": pesquisa.Pesquisa.data_pesquisa.strftime("%d-%m-%Y"),
            "id_participante_pesquisa": pesquisa.Pesquisa.id_participante_pesquisa,
            "id_status_lista_pesquisa": pesquisa.Pesquisa.id_status_lista_pesquisa,
            "observacao_pesquisa": pesquisa.Pesquisa.observacao_pesquisa,
            "data_cadastro_pesquisa": pesquisa.Pesquisa.data_cadastro_pesquisa.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_pesquisa": pesquisa.Pesquisa.data_alteracao_pesquisa.strftime("%Y-%m-%d %H:%M:%S"),
            "ident_lista": pesquisa.Lista_Restritiva.ident_lista,
            "descricao_lista": pesquisa.Lista_Restritiva.descricao_lista,
            "codigo_status": pesquisa.Status_Lista.codigo_status,
            "descricao_status": pesquisa.Status_Lista.descricao_status,
            "nome_participante": pesquisa.Participante.nome_participante,        
            "descricao_classificacao": pesquisa.Classificacao.descricao_class,        
            "id_pais": pesquisa.Pais.id_pais,        
            "pais_documento": pesquisa.Pais.nome_pais,        
            "id_documento": pesquisa.Documento.id_documento,      
            "documento": pesquisa.Documento.documento,      
            "num_doc_participante": pesquisa.Participante.num_doc_participante,  
    }

def apresenta_lista_pesquisas(pesquisas: List[ListaPesquisaSchema]):
    """ Retorna uma representação da lista das pesquisas dos participantes na lista restritiva, seguindo o schema definido em PesquisaVisualizaSchema.
    """
    result = []
    for pesquisa in pesquisas:
        result.append({
            "numero_pesquisa": pesquisa.Pesquisa.numero_pesquisa,
            "data_pesquisa": pesquisa.Pesquisa.data_pesquisa.strftime("%Y-%m-%d"),
            "data_pesquisa_fmt_br": pesquisa.Pesquisa.data_pesquisa.strftime("%d-%m-%Y"),
            "id_participante_pesquisa": pesquisa.Pesquisa.id_participante_pesquisa,
            "id_status_lista_pesquisa": pesquisa.Pesquisa.id_status_lista_pesquisa,
            "observacao_pesquisa": pesquisa.Pesquisa.observacao_pesquisa,
            "data_cadastro_pesquisa": pesquisa.Pesquisa.data_cadastro_pesquisa.strftime("%Y-%m-%d %H:%M:%S"),
            "data_alteracao_pesquisa": pesquisa.Pesquisa.data_alteracao_pesquisa.strftime("%Y-%m-%d %H:%M:%S"),
            "ident_lista": pesquisa.Lista_Restritiva.ident_lista,
            "descricao_lista": pesquisa.Lista_Restritiva.descricao_lista,
            "codigo_status": pesquisa.Status_Lista.codigo_status,
            "descricao_status": pesquisa.Status_Lista.descricao_status,
            "nome_participante": pesquisa.Participante.nome_participante,        
            "descricao_classificacao": pesquisa.Classificacao.descricao_class,        
            "id_pais": pesquisa.Pais.id_pais,        
            "pais_documento": pesquisa.Pais.nome_pais,        
            "id_documento": pesquisa.Documento.id_documento,      
            "documento": pesquisa.Documento.documento,      
            "num_doc_participante": pesquisa.Participante.num_doc_participante,        
        })

    return {"pesquisas": result}
