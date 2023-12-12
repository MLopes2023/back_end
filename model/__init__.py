from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import errorcode

# importando os elementos definidos no modelo
from model.base             import Base
from model.classificacao    import Classificacao
from model.pais             import Pais
from model.documento        import Documento
from model.participante     import Participante
from model.lista_restritiva import Lista_Restritiva
from model.pesquisa         import Pesquisa
from model.status_lista     import Status_Lista

# url de acesso ao banco 
db_url = "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD = "mysql+mysqlconnector",
    usuario = "root",
    senha = "admin",
    servidor = "localhost",
    database = "DB_MVP_SPRINT_01"
 )

# Cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# Cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# Cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
