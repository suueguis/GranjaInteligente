# granja/patrones/decorator.py
class AnimalDecorator:
    """
    Decorador base: delega atributos/métodos al animal envuelto,
    añadiendo comportamiento sin modificar la clase original.
    """
    def __init__(self, animal):
        self._animal = animal

    def __getattr__(self, name):
        return getattr(self._animal, name)

class ConVacuna(AnimalDecorator):
    def vacunado(self) -> bool:
        return True

class ConGPS(AnimalDecorator):
    def posicion(self) -> tuple[float, float]:
        # Ejemplo estático (Bogotá aprox.)
        return (4.676, -74.05)
