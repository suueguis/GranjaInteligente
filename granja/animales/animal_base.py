# granja/animales/animal_base.py
class Animal:
    def __init__(self, id: int | None = None, peso: float = 0.0):
        self.id = id
        self.peso = peso

    def __repr__(self):
        return f"<Animal id={self.id} peso={self.peso}>"
