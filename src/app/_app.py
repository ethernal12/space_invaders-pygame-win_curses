from abc import ABC, abstractmethod


class App(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def narisi(self):
        pass

    @abstractmethod
    def vnos(self):
        pass

    @abstractmethod
    def konec(self):
        pass

    @abstractmethod
    def _mapiraj(self, x: float, y: float) -> tuple[int]:
        pass
