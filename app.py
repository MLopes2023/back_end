from flask_openapi3                     import OpenAPI, Info, Tag
from flask                              import redirect
from urllib.parse                       import unquote
from sqlalchemy.exc                     import IntegrityError
from flask_cors                         import CORS
from logger                             import logger
from model                              import Participante, Pesquisa
from acessobd.bdservico                 import BdServico
from schemas                            import *
from validador.participantevalidador    import ParticipanteValidador
from validador.pesquisavalidador        import PesquisaValidador
from validador.cpf_cnpj_validador       import Cpf_Cnpj_Validador

########################################################################################################
# Apresentação documentação API
########################################################################################################

info = Info(title="API de Monitoramento de Participantes da Lista Restitiva", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

########################################################################################################
# Definição das tags
########################################################################################################

home_tag          = Tag(name="Documentação",                                description="Documentação padrão: Swagger")
pais_tag          = Tag(name="País",                                        description="Visualização dos países do documento do participante.")
classificacao_tag = Tag(name="Classificação",                               description="Visualização das classificações do participante.")
documento_tag     = Tag(name="Documento",                                   description="Visualização do tipo do documento do participante.")
identificador_tag = Tag(name="Identificador da Lista Restritiva",           description="Visualização dos identificadores da lista restritiva.")
participante_tag  = Tag(name="Participante",                                description="Adição, edição, remoção e visualização dos participantes da lista restritiva.")
pesquisa_tag      = Tag(name="Simulações das Pesquisas dos Participantes da Lista Restritia",description="Adição e visualização das simulações das pesquisas dos participantes da lista restritiva.")

########################################################################################################
# Redireciona para para /openapi estilo padrão da documentação : swagger
########################################################################################################

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela para visualização estilo padrão de documentação swagger.
    """
    return redirect('/openapi/swagger')

########################################################################################################
# Definição da rota país do documento do participante
########################################################################################################

@app.get('/ListarPaises', tags=[pais_tag],
         responses={"200": ListaPaisSchema, "404": ErrorSchema})
def get_paises():
    """Listar todos os países cadastrados.
      
    Representação da forma de retorno da lista de todos os países cadastrados.
    """
    logger.debug("Buscando lista de países.")
    
    try:

        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
        paises      = objbdacesso.get_objeto_paises()
        
        if not paises:
            return {"paises": []}, 200
            
        # Retorna a representação de todas os países cadastrados
        if paises:
            logger.debug(f"%d países econtrados" % len(paises))
            print(paises)
        else:
            logger.debug("Não existem países para listar.")
                
        return apresenta_lista_paises(paises), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca dos países cadastrados."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400
    
########################################################################################################
# Definição da rota tipo de documento do participante
########################################################################################################

@app.get('/ListarDocumentos', tags=[documento_tag],
         responses={"200": ListaDocumentoSchema, "404": ErrorSchema})
def get_documentos():
    """Listar todos os documentos cadastrados.
      
    Representação da forma de retorno da lista de todos os documentos cadastrados.
    """
    logger.debug("Buscando lista de documentos.")
    
    try:
          
        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
        documentos  = objbdacesso.get_objeto_documentos(0, "")
        
        if not documentos:
            return {"documentos": []}, 200
            
        # Retorna a representação de todas os documentos cadastrados
        if documentos:
            logger.debug(f"%d documentos econtrados" % len(documentos))
            print(documentos)
        else:
            logger.debug("Não existem documentos para listar.")
                
        return apresenta_lista_documentos(documentos), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca dos documentos cadastrados."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400
    
########################################################################################################
# Definição da rota de classificação do participante
########################################################################################################

@app.get('/ListarClassificacoes', tags=[classificacao_tag],
         responses={"200": ListaClassificacaoSchema, "404": ErrorSchema})
def get_classificacoes():
    """Listar todas as classificações do participante cadastradas.
      
    Representação da forma de retorno da lista de todas as classificações do participante cadastradas.
    """
    logger.debug("Buscando lista de classificações do participante.")
    
    try:
          
        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso     = BdServico()
        classificacoes  = objbdacesso.get_objeto_classificacoes(0)
        
        if not classificacoes:
            return {"classificacoes": []}, 200
            
        # Retorna a representação de todas os classificações cadastradas
        if classificacoes:
            logger.debug(f"%d classificações do participante econtradas." % len(classificacoes))
            print(classificacoes)
        else:
            logger.debug("Não existem classificações do participante para listar.")
                
        return apresenta_lista_classificacoes(classificacoes), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca das classificações do participante cadastradas."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400

########################################################################################################
# Definição da rota de identificadores da lista restritiva
########################################################################################################

@app.get('/ListarIdentificadoresListaRestritiva', tags=[identificador_tag],
         responses={"200": ListaRestritivaSchema, "404": ErrorSchema})
def get_identificadores_listas_restritivas():
    """Listar todos os identificadores da lista restritiva cadastrados.
      
    Representação da forma de retorno da lista de todos os identificadores da lista restritiva cadastrados.
    """
    logger.debug("Buscando lista de identificadores da lista restritiva.")
    
    try:

        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
        listas_restritivas      = objbdacesso.get_objeto_identificadores_listas_restritivas()
        
        if not listas_restritivas:
            return {"listas_restritivas": []}, 200
            
        # Retorna a representação de todas os países cadastrados
        if listas_restritivas:
            logger.debug(f"%d identificadores da lista restritiva econtrados" % len(listas_restritivas))
            print(listas_restritivas)
        else:
            logger.debug("Não existem identificadores da lista restritiva para listar.")
                
        return apresenta_lista_da_lista_restritiva(listas_restritivas), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca dos identificadores da lista restritiva cadastrados."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400
    
########################################################################################################
# Definição da rota dos status dos identificadores da lista restritiva
########################################################################################################

@app.post('/ListarStatusIdentificadoresListaRestritiva', tags=[identificador_tag],
         responses={"200": ListaStatusSchema, "404": ErrorSchema})
def post_status_identificadores_listas_restritivas(form:StatusListaIdBuscaSchema):
    """Listar um ou todos os status relacionados aos identificadores da lista restritiva cadastrados.
      
    Representação da forma de retorno de um status relacionados aos identificadores da lista restritiva ou todos cadastrados.
    """
    logger.debug("Buscando lista de status relacionados aos identificadores da lista restritiva.")
    
    try:
        # Recupera id de identificação da lista restritiva do FormSchema
        ident_lista_status = form.ident_lista_status;

        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
        status_listas      = objbdacesso.get_objeto_status_identificadores_listas_restritivas(ident_lista_status)
        
        if not status_listas:
            return {"status_listas": []}, 200
            
        # Retorna a representação de todos os status relacionados aos identificadores da lista restritiva cadastrados
        if status_listas:
            logger.debug(f"%d status relacionados aos identificadores da lista restritiva econtrados" % len(status_listas))
            print(status_listas)
        else:
            logger.debug("Não existem status relacionados aos identificadores da lista restritiva para listar.")
                
        return apresenta_lista_status_identificadores_lista_restritiva(status_listas), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca dos status relacionados aos identificadores da lista restritiva cadastrados."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400
        
########################################################################################################
# Definição das rotas dos participantes da lista restritiva
########################################################################################################

@app.post('/ListarParticipantes', tags=[participante_tag],
         responses={"200": ListaParticipante, "404": ErrorSchema})
def post_participantes(form:ParticipanteBuscaSchema):
    """Listar participante(s) da lista restritiva cadastrados que possam também satisfazer os filtros opcionais da solicitação.
      
    Representação da forma de retorno dos participante(s) da lista restritiva cadastrado(s).
    """
    logger.debug("Buscando participante(s) da lista restritiva cadastrado(s).")
    
    try:
          
        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso     = BdServico()
        
        # Recupera fitros do FormSchema
        documento_participante      =   form.documento_participante
        num_doc_participante        =   form.num_doc_participante
                
        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
        
        # Vefifica existência do documento se informado
        if documento_participante:
            objdocumento = objbdacesso.get_objeto_documentos(0, documento_participante)
            if not objdocumento:
                error_msg = "Tipo de documento de identificação %s não encontrado." % (documento_participante)
                logger.warning(f"Erro verificando existência do tipo de documento do participante : {error_msg}")
                return {"mesage": error_msg}, 409
        
        # Verifica valida documento de identificação do participante e verifica existência no cadastro de participante
        if num_doc_participante:
            # Valida CPF/CNPJ recebido
            objcpfcnpjvalidador      = Cpf_Cnpj_Validador(num_doc_participante)
            result_invalido_cpf_cnpj = objcpfcnpjvalidador.cpf_cnpj_invalido()
            if  result_invalido_cpf_cnpj:
                error_msg = result_invalido_cpf_cnpj
                logger.warning(f"Erro validando documento de identificação no participante : {error_msg}")
                return {"mesage": error_msg}, 409
    
        # Recupera participantes
        participantes  = objbdacesso.get_objeto_participantes(documento_participante, num_doc_participante )
        
        if not participantes:
            return {"participantes": []}, 200
            
        # Retorna a representação de todas os classificações cadastradas
        if participantes:
            logger.debug(f"%d participantes da lista restritiva econtrados." % len(participantes))
            print(participantes)
        else:
            logger.debug("Não existem participantes da listra restritiva para listar.")
                
        return apresenta_lista_participantes(participantes), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca dos participantes da listra restritiva cadastrados."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400
    
@app.post('/AdicionarParticipante', tags=[participante_tag],
          responses={"200": ParticipanteVisualizaSchema, "409": ErrorSchema, "400": ErrorSchema})
def adicionar_participante(form: ParticipanteFormSchema):
    """Adicionar uma novo participante da lista restritiva à base de dados.

    Representação da forma de solicitação e retorno para inserção do participante da lista restritiva.
    """

    try:
        
        # Instância um objeto da classe de acesso ao banco
        objbdacesso = BdServico()
        
        # Recupera informações recebidas FormSchema
        id_participante         = 0
        nome_participante       = form.nome_participante
        id_class_participante   = form.id_class_participante
        id_pais_doc_participante= form.id_pais_doc_participante
        id_doc_participante     = form.id_doc_participante
        num_doc_participante    = form.num_doc_participante
      
        # Valida informações recebidas do FormSchema
        validador   = ParticipanteValidador(0,nome_participante, id_class_participante, id_pais_doc_participante, id_doc_participante, 
                                              num_doc_participante,  objbdacesso.operacao_incluir)
        error_msg   = validador.mensagemvalidador
        
        if error_msg != "" and error_msg != None:
            logger.warning(f"Erro na solicitação de adição do participante da lista restritiva {error_msg}.")
            return {"mesage": error_msg}, 400

        # Verifica existência da classificação do participante
        objclassificacao = objbdacesso.get_objeto_classificacoes(id_class_participante)
        if not objclassificacao:
            error_msg = "Classificação do participante %s não encontrada." % (nome_participante)
            logger.warning(f"Erro verificando existência da classificação do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409

        # Verifica existência do país do documento do participante
        objpais = objbdacesso.get_objeto_paises(id_pais_doc_participante)
        if not objpais:
            error_msg = "País do documento do participante %s não encontrado." % (nome_participante)
            logger.warning(f"Erro verificando existência do país do documento do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409
        
        # Verifica existência do tipo do documento de identificação do participante
        objdocumento = objbdacesso.get_objeto_documentos(id_doc_participante, "")
        if not objdocumento:
            error_msg = "Tipo do documento de identificação do participante %s não encontrado." % (nome_participante)
            logger.warning(f"Erro verificando existência tipo do documento de identificação do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409

        # Critica classificação informada incompatível com o tipo de documento do participante
        # Pessoa física não pode receber como tipo de documento CNPJ
        # Pessoa jurídica não pode receber como tipo de documento CPF
        if objclassificacao.perfil_class == "F" and objdocumento.perfil_documento == "J":
            error_msg = "Classificação do participante %s incompatível com o tipo de documento de identificação informado." % (nome_participante)
            logger.warning(f"Erro validando compatibilidade da classificação com o tipo do documento de identificação do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409

        # Critica tipo de documento CPF recebido com o numero de quantidade de caracteres do número de identificação do documento
        # Critica tipo de documento CNPJ recebido com o numero de quantidade de caracteres do número de identificação do documento
        # CPF deve conter no número de identificação do documento 11 caracteres
        # CNPJ deve conter no número de identificação do documento 14 caracteres
        if objdocumento.documento == "CPF" and len(num_doc_participante) != 11:
            error_msg = "Quantidade de caracteres do CPF do participante %s inválido." % (nome_participante)
            logger.warning(f"Erro validando quantidade de caractres do CPF informado do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409
        
        if objdocumento.documento == "CNPJ" and len(num_doc_participante) != 14:
            error_msg = "Quantidade de caracteres do CNPJ do participante %s inválido." % (nome_participante)
            logger.warning(f"Erro validando quantidade de caractres do CNPJ informado do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409
   
        # Valida CPF/CNPJ recebido
        objcpfcnpjvalidador      = Cpf_Cnpj_Validador(num_doc_participante)
        result_invalido_cpf_cnpj = objcpfcnpjvalidador.cpf_cnpj_invalido()
        if  result_invalido_cpf_cnpj:
            error_msg = result_invalido_cpf_cnpj
            logger.warning(f"Erro validando documento de identificação no cadastro de participante : {error_msg}")
            return {"mesage": error_msg}, 409

        # Verifica existência do número documento de identificação do participante 
        if  objbdacesso.get_documento_participante_existe(id_pais_doc_participante, id_doc_participante, num_doc_participante, id_participante):
            error_msg = "Documento de identificação número %s já existe no cadastro de participante." % (num_doc_participante)
            logger.warning(f"Erro verificando existência do documento de identificação no cadastro de participante : {error_msg}")
            return {"mesage": error_msg}, 409

        # Iniciando processo de adição
        logger.debug(f"Adicionando participante da lista restritiva : {nome_participante}.")

        # recupera novo id do participante da lista restritiva na base de dados
        id_participante = objbdacesso.get_id_participante_novo()
        
        # adicionar registro
        objparticipante    = Participante(id_participante, nome_participante, id_class_participante, id_pais_doc_participante, id_doc_participante, num_doc_participante)
        objbdacesso.add_participante(objparticipante)
        logger.debug(f"Participante da lista restritiva {nome_participante} adicionado.")
        
        # refaz consulta com o novo registro cadastrado reconstruindo esquema de retorno
        objparticipante = objbdacesso.get_objeto_participante(id_participante)    
        
        # Retorna apresentacao conforme schema ParticipanteVisualizaSchema
        return apresenta_participante(objparticipante), 200
    
    except IntegrityError as e:
        # Tratar erro de integridade 
        error_msg = f"Erro tentando adicionar participante da lista restritiva {nome_participante}."
        logger.warning(f"Ocorreu um erro de integridade na base de dados : {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        # Caso um erro fora do previsto
        error_msg = f"Não foi possível salvar novo participante %s na base de dados." % (nome_participante)
        logger.warning(f"Erro na tentativa de adicionar novo participante: {error_msg}")
        return {"mesage": error_msg}, 400
    
@app.put('/EditarParticipante', tags=[participante_tag],
        responses={"200": ParticipanteVisualizaSchema, "409": ErrorSchema, "400": ErrorSchema})
def editar_participante(form: ParticipanteFormEditarSchema):
    """Editar um participante da lista restritiva já cadastrado.

    Representação da forma de solicitação e retorno de uma edição do cadastro do participante da lista restritiva.
    """   

    try:
        
        # Instância um objeto da classe de acesso ao banco
        objbdacesso = BdServico()
        
        # Recupera informações recebidas FormSchema
        id_participante         = form.id_participante
        nome_participante       = form.nome_participante
        id_class_participante   = form.id_class_participante
        id_pais_doc_participante= form.id_pais_doc_participante
        id_doc_participante     = form.id_doc_participante
        num_doc_participante    = form.num_doc_participante

        # Valida informações recebidas do FormSchema
        validador   = ParticipanteValidador(id_participante,        nome_participante, id_class_participante, id_pais_doc_participante, id_doc_participante, 
                                             num_doc_participante,  objbdacesso.operacao_alterar    )
        error_msg   = validador.mensagemvalidador
        
        if error_msg != "" and error_msg != None:
            logger.warning(f"Erro na solicitação de alteração do participante da lista restritiva {error_msg}.")
            return {"mesage": error_msg}, 400

        #recupera objeto Participante do id informado
        objparticipante    = objbdacesso.get_objeto_participante_Filtro_id(id_participante)
        if not objparticipante:
           error_msg = "Participante da lista restritiva id número %s não cadastrado." % (id_participante)
           logger.warning(f"Erro localizando participante da lista restritiva na base de dados : {error_msg}")
           return {"mesage": error_msg}, 404 
       
        # Verifica existência da classificação do participante
        objclassificacao = objbdacesso.get_objeto_classificacoes(id_class_participante)
        if not objclassificacao:
            error_msg = "Classificação do participante %s não encontrada." % (nome_participante)
            logger.warning(f"Erro verificando existência da classificação do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409

        # Verifica existência do país do documento do participante
        objpais = objbdacesso.get_objeto_paises(id_pais_doc_participante)
        if not objpais:
            error_msg = "País do documento do participante %s não encontrado." % (nome_participante)
            logger.warning(f"Erro verificando existência do país do documento do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409
        
       # Verifica existência do tipo do documento de identificação do participante
        objdocumento = objbdacesso.get_objeto_documentos(id_doc_participante, "")
        if not objdocumento:
            error_msg = "Tipo do documento de identificação do participante %s não encontrado." % (nome_participante)
            logger.warning(f"Erro verificando existência tipo do documento de identificação do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409

        # Critica classificação informada incompatível com o tipo de documento do participante
        # Pessoa física não pode receber como tipo de documento CNPJ
        # Pessoa jurídica não pode receber como tipo de documento CPF
        if objclassificacao.perfil_class == "F" and objdocumento.perfil_documento == "J":
            error_msg = "Classificação do participante %s incompatível com o tipo de documento de identificação informado." % (nome_participante)
            logger.warning(f"Erro validando compatibilidade da classificação com o tipo do documento de identificação do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409

        # Critica tipo de documento CPF recebido com o numero de quantidade de caracteres do número de identificação do documento
        # Critica tipo de documento CNPJ recebido com o numero de quantidade de caracteres do número de identificação do documento
        # CPF deve conter no número de identificação do documento 11 caracteres
        # CNPJ deve conter no número de identificação do documento 14 caracteres
        if objdocumento.documento == "CPF" and len(num_doc_participante) != 11:
            error_msg = "Quantidade de caracteres do CPF do participante %s inválido." % (nome_participante)
            logger.warning(f"Erro validando quantidade de caractres do CPF informado do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409
        
        if objdocumento.documento == "CNPJ" and len(num_doc_participante) != 14:
            error_msg = "Quantidade de caracteres do CNPJ do participante %s inválido." % (nome_participante)
            logger.warning(f"Erro validando quantidade de caractres do CNPJ informado do participante da lista restritiva : {error_msg}")
            return {"mesage": error_msg}, 409
        
        # Valida CPF/CNPJ recebido
        objcpfcnpjvalidador      = Cpf_Cnpj_Validador(num_doc_participante)
        result_invalido_cpf_cnpj = objcpfcnpjvalidador.cpf_cnpj_invalido()
        if  result_invalido_cpf_cnpj:
            error_msg = result_invalido_cpf_cnpj
            logger.warning(f"Erro validando documento de identificação no cadastro de participante : {error_msg}")
            return {"mesage": error_msg}, 409

        # Verifica existência do documento de identificação do participante 
        if  objbdacesso.get_documento_participante_existe(id_pais_doc_participante, id_doc_participante, num_doc_participante, id_participante):
            error_msg = "Documento de identificação número %s já existe no cadastro de participante." % (num_doc_participante)
            logger.warning(f"Erro verificando existência do documento de identificação no cadastro de participante : {error_msg}")
            return {"mesage": error_msg}, 409

        #recupera objeto participante da lista restritiva do id informado para edição
        objparticipante  = objbdacesso.get_objeto_participante_Filtro_id(id_participante)
        
        if not objparticipante:
           error_msg = f"Participante da lista restritiva id número {id_participante} nome {nome_participante} não encontrado." 
           logger.warning(f"Erro localizando participante da lista restritiva na alteração na base de dados : {error_msg}")
           return {"mesage": error_msg}, 404 
        
        # Iniciando processo de adição
        logger.debug(f"Alterando participante da lista restritiva : {objparticipante.nome_participante}.")

        # alterar campos do registro
        objbdacesso.update_participante(id_participante, nome_participante, id_class_participante, id_pais_doc_participante, id_doc_participante, num_doc_participante)
        logger.debug(f"Participante da lista restritiva {nome_participante} alterado.")
        
         # refaz consulta com o novo registro cadastrado reconstruindo esquema de retorno
        objparticipante = objbdacesso.get_objeto_participante(id_participante)    
        
        # Retorna apresentacao conforme schema ParticipanteVisualizaSchema
        return apresenta_participante(objparticipante), 200
    
    except IntegrityError as e:
        # Tratar erro de integridade 
        error_msg = f"Erro tentando alterar participante da lista restritiva {nome_participante}."
        logger.warning(f"Ocorreu um erro de integridade na base de dados : {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        # Caso um erro fora do previsto
        error_msg = f"Não foi possível alterar o participante %s na base de dados." % (nome_participante)
        logger.warning(f"Erro na tentativa de alteração participante: {error_msg}")
        return {"mesage": error_msg}, 400

@app.delete('/RemoverParticipante', tags=[participante_tag],
            responses={"200": ParticipanteDeleteSchema, "404": ErrorSchema})
def remover_participante(query: ParticipanteIdBuscaSchema):
    """Remover um participante da lista restritiva do cadastro conforme id informado.

    Representação da forma de solicitação e retorno da mensagem de confirmação de remoção do participante da lista restritiva cadastrado.
    """
    id_participante = query.id_participante
    
    try:
        
        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
       
        # Valida informacoes recebidas 
        validador   = ParticipanteValidador(id_participante, "", 0, 0, 0, "", objbdacesso.operacao_excluir    )
        error_msg   = validador.mensagemvalidador
        
        if error_msg != "" and error_msg != None:
            logger.warning(f"Erro na solicitação de exclusão do participante da lista restritiva : {error_msg}.")
            return {"mesage": error_msg}, 400

        #recupera objeto Participante do id informado
        objparticipante    = objbdacesso.get_objeto_participante_Filtro_id(id_participante)
        
        if not objparticipante:
           error_msg = "Participante da lista restritiva id número %s não cadastrado." % (id_participante)
           logger.warning(f"Erro localizando participante da lista restritiva na base de dados : {error_msg}")
           return {"mesage": error_msg}, 404 
       
        # Fazendo chamada da função para remoção
        logger.debug(f"Deletando cadastro do participante da lista restritiva id {id_participante} nome {objparticipante.nome_participante}.")
        count = objbdacesso.del_participante(id_participante)
        
        if count:
            # Retorna a representação da mensagem de confirmação
            msgremove = f"Participante da lista restritiva id {id_participante} nome {objparticipante.nome_participante} removido do cadastro."
            logger.debug(msgremove)
            return {"mensagem": msgremove }
         
    except IntegrityError as e:
        # Tratar erro de integridade ( IntegrityError )
        error_msg = "Ocorreu um erro de integridade na base de dados."
        logger.warning(f"Erro de integridade tentando remover participante da lista restritiva id {id_participante}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        # Caso um erro fora do previsto
        error_msg = f"Não foi possível remover participante da lista restritiva id {id_participante} na base de dados."
        logger.warning(f"Erro na tentativa de remoção : {error_msg}")
        return {"mesage": error_msg}, 400
    
########################################################################################################
# Definição da rota das pesquisas de participantes na lista restritiva
########################################################################################################

@app.post('/ListarSimulacoesPesquisasListaRestritiva', tags=[pesquisa_tag],
         responses={"200": ListaPesquisaSchema, "404": ErrorSchema})
def post_lista_simulacao_pesquisas_listas_restritivas(form:PesquisaBuscaSchema):
    """Listar simulações das pesquisas dos participantes da lista restritiva, que possam satisfazer os filtros de busca entre datas, sendo os demais filtros opcionais.
      
    Representação da forma de retorno da lista de simulações das pesquisas dos participantes da lista restritiva entre datas, sendo os demais filtros opcionais.
    """
    logger.debug("Buscando lista de simulações das pesquisas dos participantes da lista restritiva entre datas.")
    
    try:
        
        #Recupera filtros do Form Data    
        data_pesquisa_inicial   =   form.data_pesquisa_inicial;
        data_pesquisa_final     =   form.data_pesquisa_final;
        documento_participante  =   form.documento_participante
        num_doc_participante    =   form.num_doc_participante

        # Instância um objeto da classe de acesso ao banco de dados
        objbdacesso = BdServico()
        
        # Vefifica existência do documento se informado
        if documento_participante:
            objdocumento = objbdacesso.get_objeto_documentos(0, documento_participante)
            if not objdocumento:
                error_msg = "Tipo de documento de identificação %s não encontrado." % (documento_participante)
                logger.warning(f"Erro verificando existência do tipo de documento do participante : {error_msg}")
                return {"mesage": error_msg}, 409

        # Verifica valida documento de identificação do participante e verifica existência no cadastro de participante
        if num_doc_participante:
            # Valida CPF/CNPJ recebido
            objcpfcnpjvalidador      = Cpf_Cnpj_Validador(num_doc_participante)
            result_invalido_cpf_cnpj = objcpfcnpjvalidador.cpf_cnpj_invalido()
            if  result_invalido_cpf_cnpj:
                error_msg = result_invalido_cpf_cnpj
                logger.warning(f"Erro validando documento de identificação no participante : {error_msg}")
                return {"mesage": error_msg}, 409

        # Recupera lista conforme filtro(s) informado
        pesquisas   = objbdacesso.get_objeto_pesquisa_participantes_listas_restritivas(data_pesquisa_inicial, data_pesquisa_final, documento_participante, num_doc_participante)
        
        if not pesquisas:
            return {"pesquisas": []}, 200
        
        # Retorna a representação lista de pesquisas dos participantes da lista restritiva cadastradas
        if pesquisas:
            logger.debug(f"%d simulações das pesquisas dos participantes da lista restritiva econtrados" % len(pesquisas))
            print(pesquisas)
        else:
            logger.debug("Não existem simulações das pesquisas dos participantes da lista restritiva para listar.")
                
        return apresenta_lista_pesquisas(pesquisas), 200
    
    except Exception as e:
        error_msg = "Ocorreu um erro na busca das simulações das pesquisas dos participantes da lista restritiva cadastrados."
        logger.warning(error_msg)
        return {"mesage": error_msg}, 400

@app.post('/AdicionarSimulacaoPesquisaListaRestritiva', tags=[pesquisa_tag],
          responses={"200": PesquisaVisualizaSchema, "409": ErrorSchema, "400": ErrorSchema})
def adicionar_simulacao_pesquisa(form: PesquisaFormSchema):
    """Adicionar uma nova simulação de pesquisa do participante da lista restritiva à base de dados.

    Representação da forma de solicitação e retorno para inserção simulação de pesquisa participante da lista restritiva.
    """

    try:
        
        # Instância um objeto da classe de acesso ao banco
        objbdacesso = BdServico()
        
        # Recupera informações recebidas FormSchema
        numero_pesquisa                 = 0
        data_pesquisa                   = form.data_pesquisa
        id_participante_pesquisa        = 0
        id_pais_documento_participante  = form.id_pais_documento_participante
        documento_participante          = form.documento_participante         
        num_documento_participante      = form.num_documento_participante
        id_status_lista_pesquisa        = form.id_status_lista_pesquisa
        observacao_pesquisa             = form.observacao_pesquisa

        # Valida informações recebidas do FormSchema
        validador   = PesquisaValidador(data_pesquisa,              id_status_lista_pesquisa, 
                                        observacao_pesquisa,        id_pais_documento_participante,
                                        documento_participante,     num_documento_participante,   
                                        objbdacesso.operacao_incluir    )
        error_msg   = validador.mensagemvalidador
        
        if error_msg != "" and error_msg != None:
            logger.warning(f"Erro na solicitação de adição da simulção da pesquisa do participante da lista restritiva : {error_msg}.")
            return {"mesage": error_msg}, 400

        # Recupera dados do cadastro do participante com base no pais, tipo de documento e numero do documento     
        objdadosparticipante = objbdacesso.get_objeto_participante(0, id_pais_documento_participante, documento_participante, num_documento_participante)
        if not objdadosparticipante:
            error_msg = "Informações do %s número %s do participante não encontrado." % (documento_participante, num_documento_participante)
            logger.warning(f"Erro verificando existência de informações do participante : {error_msg}")
            return {"mesage": error_msg}, 409
        else:
            id_participante_pesquisa = objdadosparticipante.Participante.id_participante
            
        # Iniciando processo de adição
        logger.debug(f"Adicionando simulação da pesquisa do participante da lista restritiva {documento_participante} {num_documento_participante}.")

        # recupera novo numero sequencial da pesquisa na base de dados
        numero_pesquisa = objbdacesso.get_numero_pesquisa_novo()
        
        # adicionar registro
        objpesquisa = Pesquisa(numero_pesquisa, data_pesquisa, id_participante_pesquisa, id_status_lista_pesquisa, observacao_pesquisa)
        objbdacesso.add_pesquisa(objpesquisa)
        logger.debug(f"Simulação de Pesquisa da lista restritiva {documento_participante} {num_documento_participante} adicionado.")
        
        # refaz consulta com o novo registro cadastrado reconstruindo esquema de retorno
        objpesquisa = objbdacesso.get_objeto_pesquisa(numero_pesquisa)    
        
        # Retorna apresentacao conforme schema PesquisaVisualizaSchema
        return apresenta_lista_pesquisa(objpesquisa), 200
    
    except IntegrityError as e:
        # Tratar erro de integridade 
        error_msg = f"Erro tentando adicionar simulação de pesquisa da lista restritiva {documento_participante} {num_documento_participante}."
        logger.warning(f"Ocorreu um erro de integridade na base de dados : {error_msg}")
    except Exception as e:
        # Caso um erro fora do previsto
        error_msg = f"Não foi possível salvar nova simulação de Pesquisa da lista restritiva %s %s na base de dados." % (documento_participante, num_documento_participante)
        logger.warning(f"Erro na tentativa de adicionar nova pesquisa : {error_msg}")
        return {"mesage": error_msg}, 400    
    