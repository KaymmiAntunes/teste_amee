from .validators.Validator import Validator

class FaturasValidation(Validator):

    rules = {
        'uc': 'required|digits',
        'data_emissao': 'required|date_format:Y-m-d',
        'data_vencimento': 'required|date_format:Y-m-d',
        'total': 'required|numeric',
        'codigo_barras': 'required|barcode',
        'cnpj': 'required|cnpj',
    }

    messages = {
        'uc.required': 'Unidade consumidora é obrigatória.',
        'uc.digits': 'Unidade consumidora deve conter apenas números.',
        'data_emissao.required': 'Data de emissão é obrigatória.',
        'data_emissao.date_format': 'Data de emissão deve estar no formato YYYY-MM-DD.',
        'data_vencimento.required': 'Data de vencimento é obrigatória.',
        'data_vencimento.date_format': 'Data de vencimento deve estar no formato YYYY-MM-DD.',
        'total.required': 'Total é obrigatório.',
        'total.numeric': 'Total deve ser um valor numérico.',
        'codigo_barras.required': 'Código de barras é obrigatório.',
        'codigo_barras.barcode': 'Código de barras inválido.',
        'cnpj.required': 'CNPJ é obrigatório.',
        'cnpj.cnpj': 'CNPJ inválido.',
    }
