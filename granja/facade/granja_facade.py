# granja/facade/granja_facade.py
from granja.patrones.factory import crear_animal
from granja.patrones.builder import AnimalBuilder
from granja.patrones.singleton import AlimentadorGlobal

class GranjaFacade:
    def __init__(self):
        # Placeholders: subsistemas se conectarán cuando existan.
        self._ready = False

    def simular_dia(self):
        # Demo básico que siempre funciona 
        print("=== Simulación de la Granja — Facade (esqueleto) ===")
        print("1) Chequeo sensores: OK (simulado)")
        print("2) Decisión de ración: OK (simulado)")
        print("3) Dispensar alimento: OK (simulado)")
        print("4) Fin de la simulación")
