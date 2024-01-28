# Importa as bibliotecas necessárias
import os
import csv
import json
import mysql.connector
import datetime 
from flask import Flask, request, jsonify


# Função principal
def main():
    # Solicita ao usuário o caminho da pasta
    # TODO: use environment vairable instead hard-coded value
    caminho_pasta = input(r'C:\Users\DELL\Desktop\TESTE_AMEE_TI\faturas')

    # Conecta ao MySQL
    # TODO: use environment varialbes instead hard-coded values
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='teste'
    )

    # Cria uma lista com os arquivos da pasta
    arquivos = os.listdir(caminho_pasta)

    # Itera sobre os arquivos da lista
    for arquivo in arquivos:
        # Verifica se o arquivo é um arquivo JSON ou CSV
        if arquivo.endswith('.json'):
            dados = ler_arquivo_json(os.path.join(caminho_pasta, arquivo))
        elif arquivo.endswith('.csv'):
            dados = ler_arquivo_csv(os.path.join(caminho_pasta, arquivo))
        else:
            continue

        # Cria a tabela no MySQL
        criar_tabela(conexao, 'faturas', ['id', 'unidade_consumidora', 'data_referencia', 'data_emissao', 'data_vencimento', 'valor_total', 'valor_consumo', 'valor_impostos', 'codigo_barras', 'cnpj'])

        # Insere os dados na tabela
        for linha in dados:
            cursor = conexao.cursor()
            sql = f"INSERT INTO faturas (unidade_consumidora, data_referencia, data_emissao, data_vencimento, valor_total, valor_consumo, valor_impostos, codigo_barras, cnpj) VALUES ({linha[0]}, '{linha[1]}', '{linha[2]}', {linha[3]}, {linha[4]}, {linha[5]}, '{linha[6]}', '{linha[7]}')"
            cursor.execute(sql)
            conexao.commit()
            cursor.close()

        # Move o arquivo para uma pasta de consumo
        destino = os.path.join(caminho_pasta, 'consumido_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        mover_arquivo(os.path.join(caminho_pasta, arquivo), destino)

    # Fecha a conexão com o MySQL
    conexao.close()


# Inicia a aplicação Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] =False
    
# Rota de cadastro de nova fatura, utilizando o decoretor do Flask
@app.route('/faturas', methods=['POST'])
def cadastrar_fatura():
    dados_fatura = request.json

    # Valida os dados da fatura
    validos, erros = validar_dados_fatura(dados_fatura)
    if not validos:
        return jsonify({'validos': False, 'erros': erros})

    # Insere a fatura no banco de dados
    cursor = conexao.cursor()
    sql = f"INSERT INTO faturas (unidade_consumidora, data_emissao, data_vencimento, valor_total, valor_consumo, valor_impostos, codigo_barras, cnpj) VALUES ({dados_fatura['unidade_consumidora']}, '{dados_fatura['data_emissao']}', '{dados_fatura['data_vencimento']}', {dados_fatura['valor_total']}, {dados_fatura['valor_consumo']}, {dados_fatura['valor_impostos']}, '{dados_fatura['codigo_barras']}', '{dados_fatura['cnpj']}')"
    cursor.execute(sql)
    conexao.commit()
    cursor.close()

    # Retorna o identificador da fatura
    return jsonify({'id': cursor.lastrowid})

# Rota de atualização de uma fatura existente
@app.route('/faturas/<int:id>', methods=['PUT'])
def atualizar_fatura(id):
    dados_fatura = request.json

    # Valida os dados da fatura
    validos, erros = validar_dados_fatura(dados_fatura)
    if not validos:
        return jsonify({'validos': False, 'erros': erros})

    # Atualiza a fatura no banco de dados
    cursor = conexao.cursor()
    sql = f"UPDATE faturas SET unidade_consumidora='{dados_fatura['unidade_consumidora']}', data_emissao='{dados_fatura['data_emissao']}', data_vencimento='{dados_fatura['data_vencimento']}', valor_total={dados_fatura['valor_total']}, valor_consumo={dados_fatura['valor_consumo']}, valor_impostos={dados_fatura['valor_impostos']}, codigo_barras='{dados_fatura['codigo_barras']}', cnpj='{dados_fatura['cnpj']}' WHERE id={id}"
    cursor.execute(sql)
    conexao.commit()
    cursor.close()

    # Retorna o identificador da fatura
    return jsonify({'id': id})

# Rota de exclusão de uma fatura existente
@app.route('/faturas/<int:id>', methods=['DELETE'])
def excluir_fatura(id):
    # Exclui a fatura do banco de dados
    cursor = conexao.cursor()
    sql = f"DELETE FROM faturas WHERE id={id}"
    cursor.execute(sql)
    conexao.commit()
    cursor.close()

    # Retorna o status da operação
    return jsonify({'status': 'ok'})

# Rota de listagem de todas as faturas já cadastradas
@app.route('/faturas', methods=['GET'])
def listar_faturas():
    # Obtém as faturas do banco de dados
    #pra isso é necessário abrir um cursor no banco de dados
    cursor = conexao.cursor()
    sql = f"SELECT * FROM faturas"
    cursor.execute(sql)
    #depois da execução o fetchall vai retornar todos os dados que o cursor capturou
    #gerando uma lista baseada na captura
    faturas = cursor.fetchall()
    #da pra gerar com print(faturas) a exibição da tupla
    cursor.close()

    # Retorna as faturas
    return jsonify({'data': faturas})

# Rota de validação dos dados
@app.route('/faturas/validar', methods=['POST'])
def validar_fatura():
    dados_fatura = request.json

    # Valida os dados da fatura
    validos, erros = validar_dados_fatura(dados_fatura)
    return jsonify({'validos': validos, 'erros': erros})

# Função para validar os dados da fatura
def validar_dados_fatura(dados_fatura):
    # Valida a unidade consumidora
    if not dados_fatura['unidade_consumidora'].isdigit():
        return False, ['A unidade consumidora deve conter apenas números']

    # Valida as datas
    try:
        datetime.datetime.strptime(dados_fatura['data_emissao'], '%Y-%m-%d')
    except ValueError:
        return False, ['A data de emissão deve seguir o padrão ISO 8601']

    try:
        datetime.datetime.strptime(dados_fatura['data_vencimento'], '%Y-%m-%d')
    except ValueError:
        return False, ['A data de vencimento deve seguir o padrão ISO 8601']

    # Valida os valores numéricos
    for valor in ['valor_total', 'valor_consumo', 'valor_impostos']:
        if not dados_fatura[valor].replace('.', '').isdigit():
            return False, [f'O valor {valor} deve ser um número']

    # Valida o código de barras
    try:
        int(dados_fatura['codigo_barras'])
    except ValueError:
        return False, ['O código de barras deve ser um número']

    # Valida o CNPJ
    if not dados_fatura['cnpj'].replace('.', '').replace('-', '').isdigit():
        return False, ['O CNPJ deve ser um número']

    # Valida o tamanho do CNPJ
    if len(dados_fatura['cnpj']) != 14:
        return False, ['O CNPJ deve ter 14 dígitos']

    # Se chegou aqui, todos os dados são válidos
    return True, []

if __name__ == '__main__':
    app.run(debug=True)
