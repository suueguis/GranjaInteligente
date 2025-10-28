# granja/patrones/factory.py
from granja.animales.vaca import Vaca

class FactoryAnimales:
    """Crea animales según su tipo usando el patrón Factory."""

    def crear_animal(self, tipo: str, **kwargs):
        tipo = tipo.lower()
        if tipo == "vaca":
            return Vaca(**kwargs)
        raise ValueError(f"Tipo de animal no soportado: {tipo}")
