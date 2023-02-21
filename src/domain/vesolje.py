from dataclasses import dataclass

from domain.ladja import Ladja

from src.domain.vesoljci import Vesoljci


@dataclass
class Vesolje:
    sirina: int
    visina: int
    dx: int
    dy: int
    ladja: Ladja = None
    vesoljci: Vesoljci = None

    def __post_init__(self):
        self.ladja = Ladja(x=self.sirina // 2, y=self.visina // 2, dx=self.dx, dy=self.dy, velikost_x=self.sirina // 6,
                           velikost_y=self.visina // 6)

    def omejitev_ladje(self):
        if self.ladja.x >= self.sirina - 1:
            self.ladja.x = self.sirina - 1
        elif self.ladja.x <= 1:
            self.ladja.x = 1
