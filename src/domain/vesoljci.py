from dataclasses import dataclass

from src.domain.objekt import Objekt


# TODO: TUKAJ BI MOGOČE DODAL INITIALIZACIJO VELIKOSTI VESOLJCA ?
@dataclass
class Vesoljci(Objekt):
    velikost_x: float
    velikost_y: float
    hitrost: float

    def premikanje(self):
        self.x += self.hitrost
