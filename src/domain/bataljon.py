from dataclasses import dataclass, field

from src.domain.vector2D import Vector2D
from src.domain.vesoljec import Vesoljec


@dataclass
class Bataljon:
    velikost: int
    vesoljci: list[Vesoljec] = field(default_factory=list)
    razmik_vesoljcev: Vector2D = Vector2D(x=0.1, y=0.1)
    premik_vesoljca_navzdol: float = 0.1

    def __post_init__(self):
        for i in range(self.velikost):
            for j in range(2):
                vesoljec = Vesoljec(
                    x=i * self.razmik_vesoljcev.x,
                    y=j * self.razmik_vesoljcev.y,
                    sirina=0.08,
                    visina=0.08)
                self.vesoljci.append(vesoljec)

    def premik(self):
        for v in self.vesoljci:
            v.premikanje()

        menjaj_stran = False
        for vesoljec in self.vesoljci:
            if vesoljec.x >= 1:
                menjaj_stran = True
            elif vesoljec.x <= 0:
                menjaj_stran = True
        if menjaj_stran:
            for j in range(len(self.vesoljci)):
                self.vesoljci[j].y += self.premik_vesoljca_navzdol
                self.vesoljci[j].hitrost *= -1

    def najnizji(self) -> Vesoljec:
        najnizji_vesoljec = self.vesoljci[0]
        for vesoljec in self.vesoljci:
            if vesoljec.y < najnizji_vesoljec.y:
                najnizji_vesoljec = vesoljec.y

        return najnizji_vesoljec
