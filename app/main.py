from dotenv import load_dotenv
import os
from database.mysql import connect_db

load_dotenv()

connect_db()