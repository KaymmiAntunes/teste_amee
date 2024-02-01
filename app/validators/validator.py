import re
from datetime import datetime

class Validator:
    def __init__(self):
        self.rules = {
            'uc': self.validate_uc,
            'data_emissao': self.validate_date,
            'data_vencimento': self.validate_date,
            'total': self.validate_numeric,
            'codigo_barras': self.validate_barcode,
            'cnpj': self.validate_cnpj,
        }

    def validate(self, data):
        errors = {}
        for field, validator in self.rules.items():
            error = validator(data.get(field))
            if error:
                errors[field] = error
        return errors

    def validate_uc(self, value):
        if not re.match(r'^\d+$', str(value)):
            return 'Unidade consumidora deve conter apenas números, sem espaços, letras ou caracteres especiais.'

    def validate_date(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            return 'A data deve seguir o padrão ISO 8601 (YYYY-MM-DD).'

    def validate_numeric(self, value):
        try:
            float(value)
        except ValueError:
            return 'O valor deve ser numérico e usar o ponto como separador decimal.'

    def validate_barcode(self, value):
        if not re.match("^[0-9]{13}$", value):
            return "Código de barras deve conter apenas 13 números"

    def validate_cnpj(self, value):
        if not re.match("^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", value):
            return "CNPJ deve seguir o padrão 00.000.000/0000-00"
