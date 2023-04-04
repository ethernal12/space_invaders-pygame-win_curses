from dataclasses import dataclass

from src.domain.objekt import Objekt


@dataclass
class Strel(Objekt):
    hitrost: float

    def premik(self):
        self.y -= self.hitrost
