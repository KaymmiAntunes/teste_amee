from postgres import Database

# Cria uma instância da classe Database
db = Database()

def create(uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor):
    conn = db.get_connection() 
    cur = conn.cursor()
   
    insert_sql = f""" 
        INSERT INTO faturas(uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor)
        VALUES('{uc}', '{mes_referencia}', '{data_emissao}', '{data_vencimento}', {total}, '{energia_consumida}', {tarifa}, '{codigo_barras}', '{cnpj}', {valor})
        RETURNING id;
    """ 
    
    cur.execute(insert_sql)
    id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    
    return id


def update(id,data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, valor):
    conn = db.get_connection()
    cur = conn.cursor()
        
    update_sql = f"""
    UPDATE faturas
    SET data_emissao = '{data_emissao}',
        data_vencimento = '{data_vencimento}',
        total = {total},
        energia_consumida = '{energia_consumida}',
        tarifa = {tarifa},
        codigo_barras = '{codigo_barras}',
        valor = {valor}
    WHERE id = {id};
"""
    cur.execute(update_sql)
    conn.commit()
    cur.close()
    
def delete( id_fatura):
    conn = db.get_connection()
    
    cur = conn.cursor()
    delete_sql = f""" 
        DELETE FROM faturas 
        WHERE id={id_fatura};
    """ 
    cur.execute(delete_sql)
    conn.commit()
    cur.close()
    
def lister(mes_referencia):
    conn = db.get_connection()
    cur = conn.cursor()
    
    list_sql = f"""
        SELECT * FROM faturas
        WHERE mes_referencia='{mes_referencia}'
    """
    cur.execute(list_sql)
    rows = cur.fetchall()

    return rows