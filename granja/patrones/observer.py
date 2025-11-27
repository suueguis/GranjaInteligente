from __future__ import annotations
from typing import Protocol

class Observer(Protocol):
    """Interfaz para cualquier observador."""
    def update(self, message: str) -> None:
        ...

class Subject:
    """Clase que gestiona y notifica observadores."""
    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        for obs in list(self._observers):
            try:
                obs.update(message)
            except Exception as e:
                print("Observer error:", e)

class AlertObserver:
    """Observer de ejemplo: imprime cualquier mensaje recibido."""
    def update(self, message: str) -> None:
        print(f"[ALERTA] -> {message}")
