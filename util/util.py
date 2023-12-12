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
