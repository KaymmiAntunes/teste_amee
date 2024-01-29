from dotenv import load_dotenv
from database.postgres import * 
from controllers.faturas_controller import Faturas
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

load_dotenv()

db_connection = get_connection()
migrate(db_connection)

api.add_resource(Faturas, '/faturas')