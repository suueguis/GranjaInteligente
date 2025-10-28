# granja/facade/granja_facade.py
from granja.patrones.factory import FactoryAnimales
from granja.patrones.strategy import EstrategiaVerano
from granja.patrones.singleton import AlimentadorGlobal
from granja.patrones.command import DispensarCommand
from granja.patrones.observer import Subject, AlertObserver
from granja.animales.animal_base import Animal

class GranjaFacade:
    def __init__(self):
        # Inicializa los subsistemas
        self.factory = FactoryAnimales()
        self.estrategia = EstrategiaVerano()
        self.alimentador = AlimentadorGlobal.get_instance()
        self.sensor = Subject()
        self.alerta = AlertObserver()
        self.sensor.attach(self.alerta)

    def simular_dia(self):
        print("Iniciando simulación del día en la granja...")

        # Crear un animal con el Factory
        vaca = self.factory.crear_animal("vaca", id=1, peso=230.0)
        print(f"Animal creado: {vaca}")

        # Calcular la ración usando la Strategy
        racion = self.estrategia.calcular_racion(vaca.peso)
        print(f"Ración calculada: {racion:.2f} kg")

        # Dispensar alimento con Command
        comando = DispensarCommand(self.alimentador, racion)
        comando.execute()

        # Notificar sensores con Observer
        self.sensor.notify("Alimentación completada correctamente")

        print("Fin de la simulación.")
