from dataclasses import dataclass, field

from src.domain.ladja import Ladja

from src.domain.vesoljci import Vesoljci


@dataclass
class Vesolje:
    st_vrst = 2
    st_vesoljcev = 8
    premik_navzdol = 0.05
    velikost_x = 0.08
    velikost_y = 0.08
    stev_vesoljcev: list[Vesoljci] = field(default_factory=list)
    ladja: Ladja = None
    vesoljci: Vesoljci = None

    def __post_init__(self):
        self.ladja = Ladja(x=0.5,
                           y=1,
                           velikost_x=0.1,
                           velikost_y=0.1,
                           hitrost=0.009
                           )

        for i in range(self.st_vesoljcev):
            for j in range(self.st_vrst):
                self.stev_vesoljcev.append(Vesoljci(x=i / 10,
                                                    y=j / 12,
                                                    velikost_x=self.velikost_x,
                                                    velikost_y=self.velikost_y,
                                                    hitrost=0.01,
                                                    smer="desno"))

    def omejitev_ladje(self):

        if self.ladja.x >= 1:
            self.ladja.x = 1
        elif self.ladja.x <= 0:
            self.ladja.x = 0

    def menjava_smeri_vesoljcev(self):

        if self.stev_vesoljcev[-1].x >= 1:
            for j in range(len(self.stev_vesoljcev)):
                self.stev_vesoljcev[j].smer = "levo"
                self.stev_vesoljcev[j].y += self.premik_navzdol

        elif self.stev_vesoljcev[0].x <= 0:
            for k in range(len(self.stev_vesoljcev)):
                self.stev_vesoljcev[k].smer = "desno"
                self.stev_vesoljcev[k].y += self.premik_navzdol
