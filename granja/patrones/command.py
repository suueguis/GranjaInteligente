# granja/patrones/command.py
class Command:
    def execute(self):
        raise NotImplementedError

class DispensarCommand(Command):
    def __init__(self, dispenser, cantidad):
        self.dispenser = dispenser
        self.cantidad = cantidad

    def execute(self):
        # el dispenser debe exponer método dispensar(cantidad)
        self.dispenser.dispensar(self.cantidad)
