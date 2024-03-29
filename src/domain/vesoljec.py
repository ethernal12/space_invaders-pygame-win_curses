from dataclasses import dataclass

from src.domain.objekt import Objekt


@dataclass
class Vesoljec(Objekt):
    hitrost: float = 0.005

    def premikanje(self):
        self.x += self.hitrost
