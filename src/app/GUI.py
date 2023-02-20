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
        self.vesolje = Vesolje(sirina=20, visina=20)
        self.dx = 20
        self.dy = 20
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)

    def narisi_igro(self):
        pygame.display.set_caption("Space Invaders")
        # zapolni display z barvo, bela
        self.windowSurface.fill((255, 255, 100))
        # nariši ladjo
        self.vesolje.ladja.draw(self.windowSurface, self.vesolje.ladja.x * self.dx, self.vesolje.ladja.y * self.dy)
        pygame.display.update()

    def input_igralca(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    sys.exit()
        self.clock.tick(10)

    def konec(self):
        pass
