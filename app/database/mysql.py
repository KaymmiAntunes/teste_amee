import os
import mysql.connector

def connect_db():
    db_config = {
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_DATABASE"),
        "user": os.getenv("DB_USER"),
        "password":  os.getenv("DB_PASSWORD"),
        "port": 3307
    }

    print(db_config)

    connection = mysql.connector.connect(**db_config)   
    cursor = connection.cursor()

    cursor.execute("SELECT 'KAYMMI'")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
