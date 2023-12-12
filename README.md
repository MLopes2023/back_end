# API Monitor

O objetivo da API é efetuar o controle das informações referente a pessoas físicas e jurídicas, que possam constar ou não em determinadas listas de restrição para operações comerciais, crédito entre outras..
Pode ser entendido como participante da lista restritiva, estar por exemplo incluído na lista do SPC - Serviço de Proteção ao Crédito, SRF - Secretaria da Receita Federal ou até mesmo PEP - Pessoa Politicamente Exposta, sendo esse último, não ser tratado como uma grande restrição mas merecedor de atenção.
Cada lista acima mencionada está disponível para consumo de API's da própria instituição, mas como são pagas, simularemos inclusão de pessoas através do API monitor para geração de um banco de dados com uma gama de informações de restrições.

O consumo da API terá permissão dos seguintes procedimentos com os seguintes endpoints:

 1.Cadastrar e visualizar de participantes da lista restritiva, com o documento de identificação  e classificação (pessoa física ou jurídica).

Rota do Método 

/AdicionarParticipante
POST

Adicionar uma novo participante da lista restritiva à base de dados.

Layout

| CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| id_class_participante  | integer|  | Id da classificação: 1 = PF 2 = PJ 
| nome_participante| string|100  | Nome do participante da lista restritiva.
| id_pais_doc_participante| integer|  | País do documento: 1 = BRASIL
| id_doc_participante| integer|  | Id do documento: 1 = CPF 2 = CNPJ
| num_doc_participante| string|14  | Número do documento.

/EditarParticipante
PUT

Editar um participante da lista restritiva já cadastrado conforme  id do participante.

Layout

  | CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| id_participante | integer|  | Id do participante.
| id_class_participante  | integer|  | Id da classificação: 1 = PF 2 = PJ 
| nome_participante| string|100  | Nome do participante da lista restritiva.
| id_pais_doc_participante| integer|  | País do documento: 1 = BRASIL
| id_doc_participante| integer|  | Id do documento: 1 = CPF 2 = CNPJ
| num_doc_participante| string|14  | Número do documento.

/RemoverParticipante
DELETE

Layout

Remover um participante da lista restritiva do cadastro conforme id do participante.

  | CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| id_participante | integer|  | Id do participante.

/ListarParticipantes	
POST
Listar participante(s) da lista restritiva cadastrados que possam também satisfazer os filtros opcionais da solicitação.

  | CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| documento_participante| string| 10 | Documento do participante: "CPF" ou "CNPJ"
| num_doc_participante| string| 14| Número do documento do participante.

 2.Listar o cadastro de identificadores da lista restritiva com seus respectivos status.

/ListarIdentificadoresListaRestritiva 
GET
Listar todos os identificadores da lista restritiva cadastrados.

Não recebe parâmetros.

/ListarStatusIdentificadoresListaRestritiva
POST

Listar um ou todos os status relacionados aos identificadores da lista restritiva cadastrados.

  | CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| ident_lista_status| string| 15| Identificador da Lista: ""LISTA-PEP", "LISTA-SPC" OU "LISTA-SRF"

 3.Cadastrar e visualizar Simulações das Pesquisas dos Participantes da Lista Restritiva.

/AdicionarSimulacaoPesquisaListaRestritiva
POST

Adicionar uma nova simulação de pesquisa do participante da lista restritiva à base de dados.

  | CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| data_pesquisa| string| 10| data da pesquisa formato "YYYY-MM-DD".
| documento_participante| string| 10 | Documento do participante: "CPF" ou "CNPJ"
| id_pais_documento_participante| integer|  | País do documento: 1 = BRASIL
| id_status_lista_pesquisa| integer|  | Id do status do identificador da lista restritiva, podendo ser visualizada no endpoint /ListarStatusIdentificadoresListaRestritiva.
| num_documento_participante| string| 14| Número do documento do participante.
| observacao_pesquisa| string| 255| Observação da pesquisa.

/ListarSimulacoesPesquisasListaRestritiva
POST

Listar simulações das pesquisas dos participantes da lista restritiva, que possam satisfazer os filtros de busca entre datas, sendo os demais filtros opcionais.

  | CAMPO | TIPO | TAMANHO | DESCRICAO |
| -- | --| --| --|
| data_pesquisa_final| string| 10| data da pesquisa inicial formato "YYYY-MM-DD". Campo obrigatório.
| data_pesquisa_inicial| string| 10| data da pesquisa inicial formato "YYYY-MM-DD". Campo obrigatório.
| documento_participante| string| 10 | Documento do participante: "CPF" ou "CNPJ"
| num_doc_participante| string| 14| Número do documento do participante.


 - INSTALAÇÃO E EXECUÇÃO

Versão do python utilizada 3.9.

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```
Comando para instalação  das dependências/bibliotecas, descritas no arquivo `requirements.txt`.
 
Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

  


```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```
Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Observação importante:
Na primeira instalação, quando a api estiver no ar já vão ser criadas as tabelas do sistema, porém , será necessário rodar o comando insert_tables.sql na pasta sql do repositório, para que sejam inicializadas as tabelas essenciais do sistema.
O banco de dados utilizado deverá ser o mysql e segue abaixo a configuração de conexão no model.

```
# url de acesso ao banco

db_url  =  "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(

SGBD  =  "mysql+mysqlconnector",

usuario  =  "root",

senha  =  "admin",

servidor  =  "localhost",

database  =  "DB_MVP_SPRINT_01"

)
