from dataclasses import dataclass
import pygame

from src.domain.objekt import Objekt


@dataclass
class Ladja(Objekt):
    velikost_x: float
    velikost_y: float
    hitrost: float

    def levo(self):
        self.x -= self.hitrost

    def desno(self):
        self.x += self.hitrost
