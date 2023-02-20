from abc import ABC, abstractmethod

class App(ABC):
    @abstractmethod
    def inicializacija_igre(self):
        pass

    @abstractmethod
    def narisi_igro(self):
        pass

    @abstractmethod
    def input_igralca(self):
        pass

    @abstractmethod
    def konec(self):
        pass