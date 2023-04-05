from dataclasses import dataclass

from src.domain.objekt import Objekt


@dataclass
class Strel(Objekt):
    hitrost: float

    def premik_navzgor(self):
        self.y -= self.hitrost

    def premakni_navzdol(self):
        self.y += self.hitrost
