# granja/patrones/singleton.py
class AlimentadorGlobal:
    _instance = None

    def __init__(self):
        if AlimentadorGlobal._instance is not None:
            raise RuntimeError("Use get_instance()")
        self.registro = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AlimentadorGlobal()
        return cls._instance

    def dispensar(self, cantidad):
        print(f"[AlimentadorGlobal] dispensando {cantidad} kg")
        self.registro.append(cantidad)
