from datetime import datetime

class Util: 
    def __init__(self) -> None:
        pass

    # Função de validação string nula ou sem valor
    @staticmethod
    def get_str_nulo_sem_valor(strvalor:str):
    
        valorok       =  False

        if not strvalor:
            valorok = True
        elif strvalor.strip() == "":
            valorok = True

        return valorok            

    # Função de retorno conversão string data para data no formato (YYYY-MM-DD)
    @staticmethod
    def get_converte_str_data_fmt_yyyy_mm_dd(strdata:str):
    
        return datetime.strptime(strdata,"%Y-%m-%d") 
