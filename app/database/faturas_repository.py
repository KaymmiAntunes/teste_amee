def create (conn, uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor):
    cur = conn.cursor()
        
    insert_sql = f""" 
        INSERT INTO faturas(uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor)
        VALUES('{uc}', '{mes_referencia}', '{data_emissao}', '{data_vencimento}', {total}, '{energia_consumida}', {tarifa}, '{codigo_barras}', '{cnpj}', {valor});
    """ 
    
    cur.execute(insert_sql)
    conn.commit()
    cur.close()
    
def update(conn, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, valor):
    cur = conn.cursor()
        
    update_sql = f""" 
        UPDATE faturas( data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, valor)
        VALUES('{data_emissao}', '{data_vencimento}', {total}, '{energia_consumida}', {tarifa}, '{codigo_barras}', {valor});
    """ 
    
    cur.execute(update_sql)
    conn.commit()
    cur.close()
    
def delete(conn, id_fatura):
    cur = conn.cursor()
        
    delete_sql = f""" 
        DELETE FROM faturas 
        WHERE id={id_fatura};
    """ 
    
    cur.execute(delete_sql)
    conn.commit()
    cur.close()
    
def list(conn, mes_referencia):
    cur = conn.cursor()
    
    list_sql = f"""
        SELECT * FROM faturas
        WHERE mes_referencia='{mes_referencia}'
    """
    
    rows= cur.fetchall(list_sql)
    cur.close()
    
    return rows