from flask_restful import Resource
from ..database.faturas_repository import create

class Faturas(Resource):
    def post(self, uc, mes_referencia, data_emissao, data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor):
        id = create(uc, mes_referencia, data_emissao,  data_vencimento, total, energia_consumida, tarifa, codigo_barras, cnpj, valor)
        return {'id': id}, 201
    