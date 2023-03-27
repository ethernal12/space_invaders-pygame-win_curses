from dataclasses import dataclass

from src.domain.objekt import Objekt


@dataclass
class Vesoljec(Objekt):
    hitrost: float = 0.005

    def __post_init__(self):
        self.sirina = 0.08
        self.visina = 0.08

    def premikanje(self):
        self.x += self.hitrost
