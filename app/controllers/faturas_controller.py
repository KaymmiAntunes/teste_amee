from flask_restful import Resource
from flask import request
from database.faturas_repository import create

class Faturas(Resource):
    def post(self):
        body = request.json

        id = create(
            body.get('uc'),
            body.get('mes_referencia'),
            body.get('data_emissao'),
            body.get('data_vencimento'),
            body.get('total'),
            body.get('energia_consumida'),
            body.get('tarifa'),
            body.get('codigo_barras'),
            body.get('cnpj'),
            body.get('valor'),
        )
        
        return {'id': id}, 201