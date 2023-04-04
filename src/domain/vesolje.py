import math
from dataclasses import dataclass, field

from src.domain.bataljon import Bataljon
from src.domain.ladja import Ladja
from src.domain.strel import Strel


@dataclass
class Vesolje:
    ladja: Ladja = None
    bataljon: Bataljon = None
    streli: list[Strel] = field(default_factory=list)

    def __post_init__(self):
        self.ladja = Ladja(x=0.5, y=0.95, sirina=0.1, visina=0.1)
        self.bataljon = Bataljon(velikost=8)

    def spremeni(self):
        self.bataljon.premik()

        if self.ladja.x + self.ladja.sirina / 2 > 1:
            self.ladja.x = 1 - self.ladja.sirina / 2
        elif self.ladja.x - self.ladja.sirina / 2 <= 0:
            self.ladja.x = 0 + self.ladja.sirina / 2

    def kontakt_vesoljc(self):
        for strel in self.streli:
            for vesoljc in self.bataljon.vesoljci:

                strel_box = (strel.x, strel.y, strel.sirina, strel.visina)
                vesoljc_box = (vesoljc.x, vesoljc.y, vesoljc.sirina, vesoljc.visina)

                if self.prepoznaj_dotik(strel_box, vesoljc_box):
                    self.bataljon.vesoljci.remove(vesoljc)
                    self.streli.remove(strel)

    def prepoznaj_dotik(self, strel, vesoljc):
        x1, y1, w1, h1 = strel
        x2, y2, w2, h2 = vesoljc
        if (x1 <= x2 + w2 // 2 and x1 + w1 >= x2 and
                y1 <= y2 + h2 and y1 + h1 >= y2):
            return True
        else:
            return False
        # for i in range(len(self.streli)):
        #     for vesoljc in self.bataljon.vesoljci:
        #         vx = vesoljc.x
        #         vy = vesoljc.y
        #         sx = self.streli[i].x
        #         sy = self.streli[i].y
        #         rvx = round(vx, 5)
        #         rvy = round(vy, 2)
        #         rsx = round(sx, 5)
        #         rsy = round(sy, 2)
        #         print(rsy, rvy, 'strely', 'vesoljcy')
        #         # print(rsx, rsy, 'strel')
        #         if rvy == rsy and rvx == rsx:
        #             print('hit')
        #             self.bataljon.vesoljci.remove(vesoljc)

    def konec(self) -> bool:
        if self.bataljon.vesoljci:
            najnizji = self.bataljon.najnizji()
            return najnizji.y + najnizji.visina > 1
        else:
            return True
