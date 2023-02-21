from app._app import App
import sys
import pygame
from typing import Optional

from domain.vesolje import Vesolje


class GUI(App):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dx: int = 0
        self.dy: int = 0
        self.windowSurface: Optional[pygame.Surface] = None
        self.clock = pygame.time.Clock()
        self.ladja = None

    def inicializacija_igre(self):
        pygame.init()
        # scaling factor dx, dy
        self.dx = 40
        self.dy = 40
        self.vesolje = Vesolje(sirina=self.width // self.dx, visina=self.height // self.dy, dx=self.dx, dy=self.dy)
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)

    def narisi_igro(self):
        pygame.display.set_caption("Space Invaders")
        # zapolni display z barvo, bela
        self.windowSurface.fill((0, 0, 0))
        # nariši ladjo
        self.vesolje.ladja.izrisi_sliko(self.windowSurface,
                                        self.vesolje.ladja.x * self.dx - (self.vesolje.ladja.velikost_x // 2),
                                        self.width - self.vesolje.ladja.velikost_y)
        pygame.display.update()

    def input_igralca(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vesolje.ladja.premikanje(-1)
            self.vesolje.omejitev_ladje()
        elif keys[pygame.K_d]:
            self.vesolje.ladja.premikanje(1)
            self.vesolje.omejitev_ladje()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        pygame.display.update()
        self.clock.tick(10)

    def konec(self):
        pass
