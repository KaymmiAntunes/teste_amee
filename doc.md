# Projeto AMEE

## Pré-requisitos

- Python 3.11.1
- Docker e Docker Compose
- PostgreSQL

## Configuração do Ambiente

1. Clone o repositório do projeto para a sua máquina local.
2. Navegue até o diretório raiz do projeto.

## Instalação das Dependências

Instale as dependências do Python executando o seguinte comando no terminal:

-pip install psycopg2-binary, python-dotenv ,flask, flask_restful.

-------------------------------------------------------------------------------------------------
## Configuração do Banco de Dados

1. Inicie o banco de dados PostgreSQL usando o Docker Compose com o seguinte comando:

docker-compose up -d

docker ps


Você deve ver o contêiner do PostgreSQL em execução.

## Execução do Projeto

1. Execute o arquivo `main.py` com o seguinte comando:

python main.py


2. A aplicação deve estar em execução e disponível em `http://localhost:8080`.

## Testando a Aplicação

Você pode testar a aplicação usando uma ferramenta como o Postman para enviar requisições HTTP para `http://localhost:8080/faturas`.

