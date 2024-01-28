def create (conn, uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor):
    cur = conn.cursor()
        
    insert_sql = f""" 
        INSERT INTO faturas(uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor)
        VALUES('{uc}', '{mes_referencia}', '{data_emissao}', '{data_vencimento}', {total}, '{energia_consumida}', {tarifa}, '{codigo_barras}', '{cnpj}', {valor});
    """ 
    
    cur.execute(insert_sql)
    conn.commit()
    cur.close()