from app.database.faturas_repository import create

def test_cria_nova_fatura_com_dados_corretos():
    # Create a new invoice
    fatura = {
        'uc': 123456,
        'mes_referencia': "2023-07",
        'data_emissao': "2023-07-20",
        'data_vencimento': "2023-08-20",
        'total': 100.00,
        'energia_consumida': 100,
        'tarifa': 1.00,
        'codigo_barras': "1234567890123456",
        'cnpj': "123.456.789-0001-23",
        'valor': 100.00
    }

    # Save the invoice
    id_fatura = create(
        fatura['uc'],
        fatura['mes_referencia'],
        fatura['data_emissao'],
        fatura['data_vencimento'],
        fatura['total'],
        fatura['energia_consumida'],
        fatura['tarifa'],
        fatura['codigo_barras'],
        fatura['cnpj'],
        fatura['valor'],
    )

    # Check if the invoice was created with the correct data
    fatura_retornada = get(id_fatura)
    for key in fatura:
        assert fatura_retornada[key] == fatura[key], f"Valor incorreto para {key}: esperado {fatura[key]}, obtido {fatura_retornada[key]}"
