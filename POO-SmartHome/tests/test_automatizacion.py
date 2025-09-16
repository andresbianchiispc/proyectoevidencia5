from src.automatizacion import Automatizacion
from src.accion import Accion
from src.dispositivo import Dispositivo

def test_creacion_automatizacion():
    a = Automatizacion("Auto1")
    assert a.descripcion == "Auto1"
    assert a.acciones == []

def test_agregar_accion():
    a = Automatizacion("Auto2")
    acc = Accion("Encender", 1)
    a.agregar_accion(acc)
    assert acc in a.acciones

def test_ejecutar():
    a = Automatizacion("Auto3")
    acc = Accion("Encender", 1)
    a.agregar_accion(acc)
    resultados = a.ejecutar()
    assert "Realizando acción: Encender con valor: 1" in resultados