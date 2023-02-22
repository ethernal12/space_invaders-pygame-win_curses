from dataclasses import dataclass
import pygame


@dataclass
class Ladja:
    x: int
    y: int

    def premikanje(self, smer):
        self.x += smer
