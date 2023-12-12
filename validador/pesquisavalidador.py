from datetime            import datetime
from util.util           import Util
from acessobd.bdoperacao import BdOperacao

# Classe responsável pela valiadação das informações de entrada de chamadas das api's de pesquisa os participante na lista restritiva.
class PesquisaValidador:
    def __init__(self,  data_pesquisa:datetime,         id_status_lista_pesquisa:int, 
                        observacao_pesquisa,            id_pais_documento_participante,
                        documento_participante,         num_documento_participante,    
                        operacao:str):
        self.__data_pesquisa                    = data_pesquisa
        self.__id_status_lista_pesquisa         = id_status_lista_pesquisa
        self.__observacao_pesquisa              = observacao_pesquisa
        self.__id_pais_documento_participante   = id_pais_documento_participante
        self.__documento_participante           = documento_participante
        self.__num_documento_participante       = num_documento_participante
        self.__mensagem  = ""
        
        # Reupera identificação do tipo de operação
        bdOperacao      = BdOperacao()
        self.__inclusao = bdOperacao.is_inclusao(operacao)
        self.__alteracao= bdOperacao.is_alteracao(operacao)
        self.__exclusao = bdOperacao.is_exclusao(operacao)
        
        # Efetua validação
        self.__validar()
    
    @property
    def mensagemvalidador(self):
        return self.__mensagem
    
    def __validar(self):
        
        if (not self.__exclusao and (self.__data_pesquisa == None)):
            self.__mensagem = "Data da pesquisa não informada."    
        elif (not self.__exclusao and (self.__id_status_lista_pesquisa == 0 or self.__id_status_lista_pesquisa == None)):
            self.__mensagem = "Status do identificador da lista restritiva não informado."    
        elif (not self.__exclusao and (self.__id_pais_documento_participante == 0 or self.__id_pais_documento_participante == None)):
                self.__mensagem = "País do documento do participante não informado."                
        elif (not self.__exclusao  and (Util.get_str_nulo_sem_valor(self.__documento_participante))):
            self.__mensagem = "Tipo do documento do participante não informado."                            
        elif (not self.__exclusao  and (Util.get_str_nulo_sem_valor(self.__num_documento_participante))):
            self.__mensagem = "Número do documento do participante não informado."
        elif not self.__exclusao and not Util.get_str_nulo_sem_valor(self.__observacao_pesquisa):  
            if len(self.__observacao_pesquisa) > 255:   
                self.__mensagem = "Observação da pesquisa do participante na lista restritiva deve ter no máximo 100 caracteres."
