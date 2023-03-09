from dataclasses import dataclass

from src.domain.ladja import Ladja

from src.domain.vesoljci import Vesoljci


@dataclass
class Vesolje:
    ladja: Ladja = None
    vesoljci: Vesoljci = None
    stev_vesoljcev = []

    def __post_init__(self):

        self.ladja = Ladja(x=0.5,
                           y=1,
                           velikost_x=0.1,
                           velikost_y=0.1,
                           hitrost=0.009
                           )
        for i in range(1, 5):
            self.vesoljci = Vesoljci(x=i / 10,
                                     y=0,
                                     velikost_x=0.08,
                                     velikost_y=0.08,
                                     hitrost=0.01,
                                     smer="desno"
                                     )
            self.stev_vesoljcev.append(self.vesoljci)

    def omejitev_ladje(self):

        if self.ladja.x >= 1:
            self.ladja.x = 1
        elif self.ladja.x <= 0:
            self.ladja.x = 0

    def menjava_smeri_vesoljcev(self):
        for i in range(len(self.stev_vesoljcev)):
            if self.stev_vesoljcev[i].x >= 1:
                print('opa!')
                for j in range(len(self.stev_vesoljcev)):
                    self.stev_vesoljcev[j].smer = "levo"
            elif self.stev_vesoljcev[i].x <= 0:
                for k in range(len(self.stev_vesoljcev)):
                    self.stev_vesoljcev[k].smer = "desno"
