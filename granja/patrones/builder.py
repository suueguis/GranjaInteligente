# granja/patrones/builder.py
from granja.animales.animal_base import Animal

class AnimalBuilder:
    def __init__(self):
        self._args = {}

    def with_id(self, id):
        self._args['id'] = id
        return self

    def with_peso(self, peso):
        self._args['peso'] = peso
        return self

    def build(self):
        return Animal(**self._args)
