from dotenv import load_dotenv
from database.postgres import *

load_dotenv()

db_connection = connect_db()

migrate(db_connection)

print("SUCESSO")