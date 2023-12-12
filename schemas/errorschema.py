from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Definição da forma que uma mensagem de erro será representada.
    """
    mesage: str
