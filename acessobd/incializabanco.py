import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin"
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Pais ja existe")
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS DB_MVP_SPRINT_01;")

cursor.execute("CREATE DATABASE DB_MVP_SPRINT_01;")

cursor.execute("USE DB_MVP_SPRINT_01;")

# criando tabelas
TABLES = {}
TABLES['pais'] = ('''
      CREATE TABLE pais (
      id_pais SMALLINT NOT NULL,
      nome_pais varchar(50) NOT NULL,
      data_cadastro_pais DATETIME NOT NULL,
      data_alteracao_pais DATETIME NOT NULL,
      PRIMARY KEY (id_pais)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['documento'] = ('''
      CREATE TABLE documento (
      id_documento SMALLINT NOT NULL,
      documento VARCHAR(15) NOT NULL,
      id_pais_documento SMALLINT NOT NULL,
      data_cadastro_documento DATETIME NOT NULL,
      data_alteracao_documento DATETIME NOT NULL,
      PRIMARY KEY(id_documento),
      UNIQUE INDEX documento_XAK_01(documento),
      INDEX documento_FK_Index1(id_pais_documento)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print("Criando tabela {}:".format(tabela_nome), end=" ")
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print("Já existe")
            else:
                  print(err.msg)
      else:
            print("OK")

# inserindo pais
pais_sql = "INSERT INTO DB_MVP_SPRINT_01.pais (id_pais, nome_pais, data_cadastro_pais, data_alteracao_pais) VALUES (1, 'BRASIL', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
cursor.execute(pais_sql)

# select tabela pais
cursor.execute('select * from DB_MVP_SPRINT_01.pais')
print(' -------------  pais:  -------------')
for user in cursor.fetchall():
    print(user[0],user[1],user[2], user[3] )

# inserindo documento
documento_sql = "INSERT INTO DB_MVP_SPRINT_01.documento (id_documento, documento, id_pais_documento, data_cadastro_documento, data_alteracao_documento) VALUES (1, 'CPF', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
cursor.execute(documento_sql)

# select tabela documento
cursor.execute('select * from DB_MVP_SPRINT_01.documento')
print(' -------------  documento:  -------------')
for user in cursor.fetchall():
    print(user[0],user[1],user[2], user[3], user[4])
    
# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()