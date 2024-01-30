from app.models import Fatura

def test_cria_nova_fatura_com_dados_corretos():
    # Cria uma nova fatura
    fatura = Fatura()
    fatura.uc = 123456
    fatura.mes_referencia = "2023-07"
    fatura.data_emissao = "2023-07-20"
    fatura.data_vencimento = "2023-08-20"
    fatura.total = 100.00
    fatura.energia_consumida = 100
    fatura.tarifa = 1.00
    fatura.codigo_barras = "1234567890123456"
    fatura.cnpj = "123.456.789-0001-23"

    # Salva a fatura
    fatura.save()

    # Verifica se a fatura foi criada com os dados corretos
    fatura_retornada = Fatura.objects.get(id=fatura.id)
    assert fatura_retornada.uc == fatura.uc
    assert fatura_retornada.mes_referencia == fatura.mes_referencia
    assert fatura_retornada.data_emissao == fatura.data_emissao
    assert fatura_retornada.data_vencimento == fatura.data_vencimento
    assert fatura_retornada.total == fatura.total
    assert fatura_retornada.energia_consumida == fatura.energia_consumida
    assert fatura_retornada.tarifa == fatura.tarifa
    assert fatura_retornada.codigo_barras == fatura.codigo_barras
    assert fatura_retornada.cnpj == fatura.cnpj
