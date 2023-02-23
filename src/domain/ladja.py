from dataclasses import dataclass
import pygame


@dataclass
class Ladja:
    x: float
    y: float
    velikost_x: float
    velikost_y: float
    hitrost: float

    def levo(self):
        self.x -= self.hitrost

    def desno(self):
        self.x += self.hitrost
