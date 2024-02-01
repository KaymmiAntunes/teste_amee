import sys
sys.path.insert(0, 'C:\\Users\\DELL\\Desktop\\TESTE_AMEE_TI\\app\\database')

from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask
from database import faturas_repository
from validators import faturas_validation
from postgres_repo import Database
from controllers.faturas_controller import Faturas

# Cria uma instância da classe Database
db = Database()

app = Flask(__name__)
api = Api(app)

# Cria a conexão com o banco de dados
db_connection = db.get_connection()

# Realiza a migração
db.migrate()

# Adiciona os recursos da API
api.add_resource(Faturas, '/faturas') #Rota para manipular todas as faturas
api.add_resource(Faturas, '/faturas/<int:id>', endpoint='faturas_id') # rota para manipular uma fatura específica por ID
api.add_resource(Faturas, '/faturas/mes/<string:mes_referencia>', endpoint='faturas_mes_referencia')#rota para listar faturas de um mês específico

# Configurações da aplicação
app.config['APP_NAME'] = 'API de faturas de energia'
app.config['PORT'] = 8080
app.config['ENV'] = 'development'

# Executa o aplicativo
if __name__ == "__main__":
    app.run(debug=True, port=app.config['PORT'])

