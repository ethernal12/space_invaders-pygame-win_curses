from dataclasses import dataclass

from src.domain.ladja import Ladja

from src.domain.vesoljci import Vesoljci


@dataclass
class Vesolje:
    ladja: Ladja = None
    vesoljci: Vesoljci = None

    def __post_init__(self):

        self.ladja = Ladja(x=0.5, y=1, velikost_x=0.1, velikost_y=0.1, hitrost=0.003)

    def omejitev_ladje(self):

        if self.ladja.x >= 1:
            self.ladja.x = 1
        elif self.ladja.x <= 0:
            self.ladja.x = 0
