from dotenv import load_dotenv
from database.postgres import * 
from controllers.faturas_controller import Faturas
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)

load_dotenv()

db_connection = get_connection()
migrate(db_connection)

api.add_resource(Faturas, '/faturas')
api.add_resource(Faturas, '/faturas/<int:id>')
api.add_resource(Faturas, '/faturas/<int:id>')
api.add_resource(Faturas, '/faturas/<string:mes_referencia>')

if __name__ =='__main__':
    app.run(debug=True)