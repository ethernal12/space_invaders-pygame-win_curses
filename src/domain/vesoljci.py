from dataclasses import dataclass

from src.domain.objekt import Objekt

# TODO: TUKAJ BI MOGOČE DODAL INITIALIZACIJO VELIKOSTI VESOLJCA ?
@dataclass
class Vesoljci(Objekt):
    velikost_x: float
    velikost_y: float
    hitrost: float
    smer: str

    def premikanje(self):
        if self.smer == "desno":
            self.x += self.hitrost
        elif self.smer == "levo":
            self.x -= self.hitrost
