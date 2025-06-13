from .observer import Observer

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            return
        # poner error no se me ocurre ahora
        # segunda opcion mandarlo a un log, puede ser
        # bastante recomedable
    def delete_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            return
        # poner error no se me ocurre ahora

    def notify_observers(self):
        for observer in self._observers:
            observer.update()
