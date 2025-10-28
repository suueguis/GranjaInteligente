# granja/main.py
from granja.facade.granja_facade import GranjaFacade

if __name__ == "__main__":
    granja = GranjaFacade()
    granja.simular_dia()
