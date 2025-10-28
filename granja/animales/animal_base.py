# granja/animales/animal_base.py
from dataclasses import dataclass

@dataclass
class Animal:
    id: int
    peso: float

    def __str__(self) -> str:
        return f"Animal(id={self.id}, peso={self.peso})"
