# granja/patrones/observer.py
from __future__ import annotations
from typing import Protocol


class Observer(Protocol):
    def update(self, message: str) -> None: ...


class AlertObserver:
    """Observer de ejemplo: imprime cualquier mensaje recibido."""
    def update(self, message: str) -> None:
        print(f"AlertObserver:", message)
