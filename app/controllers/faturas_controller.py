from flask_restful import Resource
from flask import request, abort
from database.faturas_repository import create, update, delete, lister
import re
from datetime import datetime

class Faturas(Resource):
    def post(self):
        body = request.json
        self.validate(body)
        
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
        self.validate(body)
        
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
    
   
    def validate(self, body):
    # This field should contain only numbers
    if not re.match("^[0-9]+$", body.get('uc')):
        abort(400, "UC should contain only numbers")

    # Dates: All should follow the ISO 8601 date standard
    date_format = "%Y-%m-%dT%H:%M:%S"
    for date_field in ['mes_referencia', 'data_emissao', 'data_vencimento']:
        try:
            datetime.strptime(body.get(date_field), date_format)
        except ValueError:
            abort(400, f"{date_field} should be in ISO 8601 format")

    # Numeric values: All numeric values must adhere to the decimal standard
    for num_field in ['total', 'energia_consumida', 'tarifa', 'valor']:
        if not isinstance(body.get(num_field), (int, float)):
            abort(400, f"{num_field} should be a number")

    # Barcode: It is necessary to create a validation that confirms that the barcode has no inconsistency
    if not re.match("^[0-9]{13}$", body.get('codigo_de_barras')):
        abort(400, "Código de barras deve conter apenas 13 números")

    # CNPJ: Must follow the standard using the common mask of a CNPJ
    if not re.match("^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", body.get('cnpj')):
        abort(400, "CNPJ deve seguir o padrão 00.000.000/0000-00")
