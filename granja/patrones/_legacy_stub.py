# granja/patrones/_legacy_stub.py
class LegacySensor:
    """Simula un sensor 'legacy' con API read_value()."""
    def read_value(self):
        # Ejemplo simple; en real podría venir de hardware/archivo/red
        return {"lvl": 18}
