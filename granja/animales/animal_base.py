# granja/animales/animal_base.py
from dataclasses import dataclass

@dataclass
class Animal:
    id: int | None = None
    peso: float = 0.0

    def __str__(self) -> str:
        return f"Animal id={self.id} peso={self.peso}"
