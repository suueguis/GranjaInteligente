# granja/patrones/adapter.py
from __future__ import annotations
from typing import Any, List
from granja.patrones.observer import Observer


class SensorLegacyAdapter:
    """
    Adapter para un sensor 'legacy' cuya API es read_value() -> dict.
    Traduce la clave 'lvl' a un mensaje 'nivel X' y notifica a los observers.
    """

    def __init__(self, legacy_sensor: Any):
        self._legacy = legacy_sensor
        self._observers: List[Observer] = []

    def attach(self, obs: Observer) -> None:
        if obs not in self._observers:
            self._observers.append(obs)

    def detach(self, obs: Observer) -> None:
        if obs in self._observers:
            self._observers.remove(obs)

    def _notify(self, msg: str) -> None:
        # Copia para evitar problemas si un observer se desuscribe durante update()
        for o in list(self._observers):
            try:
                o.update(msg)
            except Exception:
                # Aísla fallos de observers individuales
                pass

    def check_and_notify(self) -> None:
        """Lee del sensor legacy y notifica con el formato estándar."""
        try:
            data = self._legacy.read_value()
        except Exception as e:
            self._notify(f"error leyendo sensor: {type(e).__name__}")
            return

        nivel = None if not isinstance(data, dict) else data.get("lvl", None)
        if nivel is None:
            self._notify("dato 'lvl' ausente")
            return

        self._notify(f"nivel {nivel}")
