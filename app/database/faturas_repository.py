from database.postgres import get_connection


def create(uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor):
    conn = get_connection()
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


def update(data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, valor):
    conn = get_connection()
    cur = conn.cursor()
        
    update_sql = f""" 
        UPDATE faturas( data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, valor)
        VALUES('{data_emissao}', '{data_vencimento}', {total}, '{energia_consumida}', {tarifa}, '{codigo_barras}', {valor});
    """ 
    
    cur.execute(update_sql)
    conn.commit()
    cur.close()
    
def delete( id_fatura):
    conn = get_connection()
    cur = conn.cursor()
        
    delete_sql = f""" 
        DELETE FROM faturas 
        WHERE id={id_fatura};
    """ 
    
    cur.execute(delete_sql)
    conn.commit()
    cur.close()
    
def list(mes_referencia):
    conn = get_connection()
    cur = conn.cursor()
    
    list_sql = f"""
        SELECT * FROM faturas
        WHERE mes_referencia='{mes_referencia}'
    """
    
    rows= cur.fetchall(list_sql)
    cur.close()
    
    return rows