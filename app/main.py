from dotenv import load_dotenv
from database.postgres import * 

load_dotenv()

db_connection = get_connection()
migrate(db_connection)

print("SUCESSO")