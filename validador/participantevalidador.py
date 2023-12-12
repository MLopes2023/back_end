from util.util           import Util
from acessobd.bdoperacao import BdOperacao

# Classe responsável pela valiadação das informações de entrada de chamadas das api's do participante da lista restritiva.
class ParticipanteValidador:
    def __init__(self,  id_participante:int,     nome_participante:str,     id_class_participante:int, id_pais_doc_participante:int, 
                        id_doc_participante:int, num_doc_participante:str,  operacao:str):
        self.__id_participante          = id_participante
        self.__nome_participante        = nome_participante
        self.__id_class_participante    = id_class_participante
        self.__id_pais_doc_participante = id_pais_doc_participante
        self.__id_doc_participante      = id_doc_participante
        self.__num_doc_participante     = num_doc_participante
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
        
        if (not self.__inclusao and (self.__id_participante == 0 or self.__id_participante == None)):
            self.__mensagem = "id do participante igual a zero ou não informado."    
        elif (not self.__exclusao  and (Util.get_str_nulo_sem_valor(self.__nome_participante))):
            self.__mensagem = "Nome do participante da lista restritiva não informado."    
        elif not self.__exclusao and len(self.__nome_participante) > 50:   
            self.__mensagem = "Nome do participante da lista restritiva deve ter no máximo 100 caracteres."
        elif (not self.__exclusao and (self.__id_class_participante == 0 or self.__id_class_participante == None)):
            self.__mensagem = "Classificação do participante não informada."    
        elif (not self.__exclusao and (self.__id_pais_doc_participante == 0 or self.__id_pais_doc_participante == None)):
            self.__mensagem = "País do documento do participante não informado."                
        elif (not self.__exclusao and (self.__id_doc_participante == 0 or self.__id_doc_participante == None)):
            self.__mensagem = "Tipo do documento do participante não informado."                            
        elif (not self.__exclusao  and (Util.get_str_nulo_sem_valor(self.__num_doc_participante))):
            self.__mensagem = "Número do documento do participante não informado."
       