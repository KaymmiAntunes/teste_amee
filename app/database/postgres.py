import os
import psycopg2

def connect_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )   

database_schemma = """
CREATE TABLE IF NOT EXISTS faturas(
    id SERIAL PRIMARY KEY,
    uc VARCHAR(32) NOT NULL,
    mes_referencia DATE NOT NULL,
    data_emissao DATE NOT NULL,
    data_vencimento DATE NOT NULL,
    total DECIMAL(5, 2) NOT NULL,
    energia_consumida INTEGER NOT NULL,
    tarifa DECIMAL(10,8) NOT NULL,
    codigo_barras VARCHAR(56) NOT NULL,
    cnpj VARCHAR(14) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);
""" 

def migrate(conn):
    cur = conn.cursor()
    
    cur.execute(database_schemma)
    conn.commit()
    
    cur.close()