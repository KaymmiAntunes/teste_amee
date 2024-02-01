# 🚀 Projeto AMEE

# TESTE AMEE

## To Do
- [x] Criar Docker Compose para o MySQL
- [x] Carregar variáveis de ambiente a partir do arquivo .env
- [x] Conectar com o banco de dados
- [x] Implementar a camada repository
- [x] Implementar a camada de service
- [x] Implementar endpoints
- [x] Criar documentação de requisitos

## 📋 Pré-requisitos

- Python 3.11.1
- Docker e Docker Compose
- PostgreSQL

## 🛠️ Configuração do Ambiente

1. Clone o repositório do projeto para a sua máquina local.
2. Navegue até o diretório raiz do projeto.

## 📦 Instalação das Dependências

Instale as dependências do Python executando o seguinte comando no terminal:

```bash
pip install psycopg2-binary python-dotenv flask flask_restful

🗄️ Configuração do Banco de Dados
Inicie o banco de dados PostgreSQL usando o Docker Compose com o seguinte comando:

docker-compose up -d
docker ps

Você deve ver o contêiner do PostgreSQL em execução.

🚀 Execução do Projeto
Execute o arquivo main.py com o seguinte comando:

python main.py

# 📁 Estrutura do Projeto

O projeto tem a seguinte estrutura de diretórios e arquivos:

- `README.md`: Contém as instruções básicas para a instalação e execução do projeto.
- `dockerfile`: Usado para criar uma imagem Docker para o projeto.
- `docker-compose.yml`: Define os serviços que compõem o aplicativo.
- `.gitignore`: Especifica os arquivos e diretórios que o Git deve ignorar.
- `.env`: Contém as variáveis de ambiente necessárias para o projeto.
- `faturas`: Diretório que contém os dados das faturas em formatos CSV e JSON.
- `app`: Diretório principal do aplicativo, que contém:
  - `controllers`: Contém o controlador para as faturas.
  - `database`: Contém os repositórios para as faturas e o PostgreSQL.
  - `validator`: Contém os validadores para as faturas.
  - `main.py`: Ponto de entrada do aplicativo.

# 🧪 Testando a API

Para testar a API, você pode usar uma ferramenta como o Postman ou o cURL. A aplicação deve estar em execução e disponível em `http://localhost:8080`. Aqui estão alguns exemplos de como você pode fazer isso:

- Para criar uma nova fatura, você pode enviar uma solicitação POST para `/faturas` com o corpo da solicitação contendo os detalhes da fatura.
- Para atualizar uma fatura existente, você pode enviar uma solicitação PUT para `/faturas/<id>` com o corpo da solicitação contendo os novos detalhes da fatura.
- Para excluir uma fatura, você pode enviar uma solicitação DELETE para `/faturas/<id>`.
- Para listar todas as faturas de um mês específico, você pode enviar uma solicitação GET para `/faturas/mes/<mes_referencia>`.

Quando você cria, atualiza ou exclui uma fatura através da API, as alterações são refletidas no banco de dados. Você pode verificar isso consultando o banco de dados diretamente.
