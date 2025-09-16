from src.accion import Accion
import pytest


def test_crear_accion():
    accion = Accion("comprar", 100)
    assert accion.tipo_accion == "comprar"
    assert accion.valor_configurado == 100


def test_str():
    accion = Accion("vender", 50)
    assert str(accion) == "Accion: vender, Valor Configurado: 50"


def test_getters():
    accion = Accion("comprar", 200)
    assert accion.get_tipo_accion() == "comprar"
    assert accion.get_valor_configurado() == 200


def test_setters():
    accion = Accion("comprar", 100)
    accion.set_tipo_accion("vender")
    accion.set_valor_configurado(150)
    
    assert accion.get_tipo_accion() == "vender"
    assert accion.get_valor_configurado() == 150


def test_realizar_accion():
    accion = Accion("comprar", 75)
    resultado = accion.realizar_accion()
    assert resultado == "Realizando acción: comprar con valor: 75"