from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask
from database import faturas_repository
from validators import faturas_validation
from app.database.faturas_repository import get_connection, migrate
from app.controllers.faturas_controller import Faturas

app = Flask(__name__)
api = Api(app)

# Cria a conexão com o banco de dados
db_connection = get_connection()
migrate(db_connection)

# Adiciona os recursos da API
api.add_resource(Faturas, '/faturas')
api.add_resource(Faturas, '/faturas/<int:id>', endpoint='faturas_id')
api.add_resource(Faturas, '/faturas/mes/<string:mes_referencia>', endpoint='faturas_mes_referencia')

# Configurações da aplicação
app.config['APP_NAME'] = 'API de faturas de energia'
app.config['PORT'] = 8080
app.config['ENV'] = 'development'

# Executa o aplicativo
if __name__ == "__main__":
    app.run(debug=True)

