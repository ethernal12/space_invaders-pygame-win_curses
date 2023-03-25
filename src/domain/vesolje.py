from dataclasses import dataclass, field

from src.domain.bataljon import Bataljon
from src.domain.ladja import Ladja


@dataclass
class Vesolje:
    ladja: Ladja = None
    bataljon: Bataljon = None

    def __post_init__(self):
        self.ladja = Ladja(x=0.5, y=0.95, sirina=0.1, visina=0.1)
        self.bataljon = Bataljon(velikost=8)

    def spremeni(self):
        self.bataljon.premik()

        if self.ladja.x + self.ladja.sirina / 2 > 1:
            self.ladja.x = 1 - self.ladja.sirina
        elif self.ladja.x - self.ladja.sirina / 2 <= 0:
            self.ladja.x = 0 + self.ladja.sirina

    def konec(self) -> bool:
        najnizji = self.bataljon.najnizji()
        return najnizji.y > 1


