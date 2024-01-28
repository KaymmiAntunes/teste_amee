from dotenv import load_dotenv
from database.postgres import connect_db

load_dotenv()

connect_db()