import pytest
from app.descuentos import calcular_precio_final


def test_descuento_exitoso():
    resultado = calcular_precio_final(1000, 20)
    assert resultado == 800


def test_precio_negativo_error():
    with pytest.raises(ValueError):
        calcular_precio_final(-500, 10)


def test_descuento_cien_por_ciento():
    resultado = calcular_precio_final(1500, 100)
    assert resultado == 0