# granja/patrones/state.py
class EstadoAnimal:
    def descripcion(self):
        return "estado genérico"

class EstadoSano(EstadoAnimal):
    def descripcion(self):
        return "sano"

class EstadoEnfermo(EstadoAnimal):
    def descripcion(self):
        return "enfermo"
