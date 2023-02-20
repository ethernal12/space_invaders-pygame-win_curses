from dataclasses import dataclass

from domain.ladja import Ladja


class Vesoljci:
    pass


@dataclass
class Vesolje:
    sirina: int
    visina: int
    ladja: Ladja = None
    vesoljci: Vesoljci = None

    def __post_init__(self):
        self.ladja = Ladja(x=self.sirina // 2, y=self.visina // 2, dx=0, dy=0)
