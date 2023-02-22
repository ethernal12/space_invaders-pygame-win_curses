from dataclasses import dataclass
import pygame


@dataclass
class Ladja:
    x: int
    y: int
    velikost_x: int
    velikost_y: int

    def premikanje(self, smer):
        self.x += smer
