from flask_restful import Resource
from flask import request
from .database.faturas_repository import create, update, delete, lister
from .validators.faturas_validation import FaturasValidation

class Faturas(Resource):

    def post(self):
        body = request.json

        # Valida os dados de entrada
        validator = FaturasValidation()
        errors = validator.validate(body)
        if errors:
            return {"message": "Erro de validação.", "errors": errors}, 400

        # Cria a fatura
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

    def put(self, id):
        # update
        body = request.json

        validator = FaturasValidation()
        errors = validator.validate(body)
        if errors:
            return {"message": "Erro de validação.", "errors": errors}, 400

        success = update(
            id,
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

        return {'id': id}, 200 if success else 404
        
    def delete(self, id):
        # call delete
        success = delete(id)

        return {'id': id}, 204 if success else 404
        
    def get(self, mes_referencia):
        #Returns a list of invoices for the specified month.

        invoices = lister(mes_referencia)

        if invoices:
            return invoices, 200
        else:
            return {'message': 'No invoice found for the month specified.'}, 404
