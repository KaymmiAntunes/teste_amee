from dotenv import load_dotenv
from database.postgres import get_connection, migrate
from controllers.faturas_controller import Faturas
from flask_restful import Api
from flask import Flask
from app.tests import test_cria_nova_fatura_com_dados_corretos

app = Flask(__name__)
api = Api(app)

load_dotenv()

# Cria a conexão com o banco de dados
db_connection = get_connection()
migrate(db_connection)

# Adiciona os recursos da API
api.add_resource(Faturas, '/faturas')
api.add_resource(Faturas, '/faturas/<int:id>', endpoint='faturas_id')
api.add_resource(Faturas, '/faturas/mes/<string:mes_referencia>', endpoint='faturas_mes_referencia')

# Executa o teste
if __name__ == "__main__":
    test_cria_nova_fatura_com_dados_corretos()
    app.run(debug=True)
