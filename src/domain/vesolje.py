from dataclasses import dataclass

from src.domain.ladja import Ladja

from src.domain.vesoljci import Vesoljci
from src.utils import config


@dataclass
class Vesolje:
    ladja: Ladja = None
    vesoljci: Vesoljci = None

    def __post_init__(self):
        config.init()
        self.ladja = Ladja(x=config.CONFIG.pozicija_ladje_x,
                           y=config.CONFIG.pozicija_ladje_y,
                           velikost_x=config.CONFIG.velikost_ladje_x,
                           velikost_y=config.CONFIG.velikost_ladje_y,
                           hitrost=config.CONFIG.hitrost_ladje
                           )

    def omejitev_ladje(self):

        if self.ladja.x >= 1:
            self.ladja.x = 1
        elif self.ladja.x <= 0:
            self.ladja.x = 0
