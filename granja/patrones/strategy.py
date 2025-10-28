# granja/patrones/strategy.py

class EstrategiaAlimentacion:
    """Interfaz base para las estrategias de alimentación."""

    def calcular_racion(self, peso: float) -> float:
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class EstrategiaVerano(EstrategiaAlimentacion):
    """Estrategia de alimentación para verano."""

    def calcular_racion(self, peso: float) -> float:
        # En verano los animales comen menos (3% de su peso)
        return peso * 0.03


class EstrategiaInvierno(EstrategiaAlimentacion):
    """Estrategia de alimentación para invierno."""

    def calcular_racion(self, peso: float) -> float:
        # En invierno comen más (5% de su peso)
        return peso * 0.05
