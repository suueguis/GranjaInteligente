# granja/patrones/factory.py
from granja.animales.vaca import Vaca

def crear_animal(tipo: str, **kwargs):
    tipo = tipo.lower()
    if tipo == "vaca":
        return Vaca(**kwargs)
    raise ValueError(f"Tipo de animal no soportado: {tipo}")
