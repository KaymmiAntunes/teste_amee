# upload_faturas.py
import os
import json
import requests

def upload_faturas():
    # Diretório onde os arquivos JSON estão armazenados
    diretorio = 'C:\\Users\\DELL\\Desktop\\TESTE_AMEE_TI\\app\\fatura'

    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # URL da API
    url = "http://localhost:8080/faturas"

    # Percorre todos os arquivos
    for arquivo in arquivos:
        # Verifica se o arquivo é um arquivo JSON
        if arquivo.endswith('.json'):
            # Abre o arquivo JSON
            with open(os.path.join(diretorio, arquivo), 'r') as f:
                # Carrega os dados do arquivo JSON
                data = json.load(f)
                
                # Envia os dados para a API
                response = requests.post(url, json=data)
                
                # Verifica se a solicitação foi bem-sucedida
                if response.status_code == 200:
                    print(f'Os dados do arquivo {arquivo} foram enviados com sucesso para a API.')
                else:
                    print(f'Houve um erro ao enviar os dados do arquivo {arquivo} para a API.')
