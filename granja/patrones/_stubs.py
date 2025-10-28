# granja/patrones/_stubs.py
class DispenserStub:
    def __init__(self):
        self.log = []

    def dispensar(self, cantidad):
        print(f"[DispenserStub] dispensando {cantidad} kg")
        self.log.append(cantidad)
