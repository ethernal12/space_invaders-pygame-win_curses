from dataclasses import dataclass
import pygame


@dataclass
class Ladja:
    x: int
    y: int
    dx: int
    dy: int
    velikost_x: int
    velikost_y: int

    def __post_init__(self):
        self.velikost_x *= self.dx
        self.velikost_y *= self.dy
        self.slika = pygame.image.load("src/domain/ladja.png")
        self.nastavi_velikost_slike = pygame.transform.scale(self.slika,
                                                             (self.velikost_x, self.velikost_y))

    def izrisi_sliko(self, screen, x, y):
        screen.blit(self.nastavi_velikost_slike, (x, y))

    def premikanje(self, smer):
        self.x += smer
