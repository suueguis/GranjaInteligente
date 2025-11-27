# granja/patrones/observer.py
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        for obs in list(self._observers):
            try:
                obs.update(message)
            except Exception as e:
                print("Observer error:", e)

# ejemplo de observer
class AlertObserver:
    def update(self, message):
        print("[ALERTA] ->", message)
