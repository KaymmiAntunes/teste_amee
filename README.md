** 🚀 Projeto AMEE**

Este projeto é uma API RESTful para gerenciamento de faturas de energia. Ele é desenvolvido em Python, usando o framework Flask.

Pendência

- [x] Criar Docker Compose para o PostgresSQL
- [x] Carregar variáveis de ambiente a partir de arquivo .env
- [x] Conectar com o banco de dados
- [x] Implementar a camada repository
- [x] Implementar a camada de service
- [x] Implementar endpoints
- [x] Criar documentação de requisitos

📋 Pré-requisitos

Pitão 3.11.1
Docker e Docker Compose
PostgreSQL

🛠️ Configuração do Ambiente

  . Clone o repositório do projeto para a sua máquina local.
  . Navegue até o diretório raiz do projeto.
  . Instalação das Dependências

📦 Instale as dependências do Python executando o seguinte comando no terminal:

    pip install psycopg2-binary python-dotenv flask flask_restful
    Configuração do Banco de Dados

🗄️ Inicie o banco de dados PostgreSQL usando o Docker Compose com o seguinte comando:

    docker-compose up -d
    docker ps

Você deve ver o contêiner do PostgreSQL em execução.

🚀 Execução do Projeto

    Execute o arquivo main.py com o seguinte comando:
    python main.py
    O projeto estará em execução em http://localhost:8080.

📁 Estrutura do Projeto

O projeto tem a seguinte estrutura de diretórios e arquivos:

.
├── README.md
├── dockerfile
├── docker-compose.yml
├── .gitignore
├── .env
├── faturas
│   ├── faturas.csv
│   └── faturas.json
└── app
    ├── controllers
    │   └── faturas.py
    ├── database
    │   ├── faturas_repository.py
    │   └── postgres_repository.py
    ├── validator
    │   └── faturas_validator.py
    └── main.py

Testando 🧪a API

Para testar a API, você pode usar uma ferramenta como o Postman ou o cURL.

Aqui estão alguns exemplos de como você pode fazer isso:

    .Para criar uma nova fatura, você pode enviar uma solicitação POST para /faturas com o corpo da solicitação contendo os detalhes da fatura.
    .Para atualizar uma fatura existente, você pode enviar uma solicitação PUT para /faturas/<id> com o corpo da solicitação contendo os novos  detalhes da fatura.
    .Para excluir uma fatura, você pode enviar uma solicitação DELETE para /faturas/<id>.
    .Para listar todas as faturas de um mês específico, você pode enviar uma solicitação GET para /faturas/mes/<mes_referencia>.

Quando você cria, atualiza ou exclui uma fatura através da API, as alterações são refletidas no banco de dados. Você pode verificar isso consultando o banco de dados diretamente.
