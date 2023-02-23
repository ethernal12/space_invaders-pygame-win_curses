from src.app._app import App
import sys
import pygame
from typing import Optional

from src.domain.vesolje import Vesolje


class GUI(App):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.windowSurface: Optional[pygame.Surface] = None
        self.clock = pygame.time.Clock()
        self.ladja = None

    def init(self):
        pygame.init()
        self.vesolje = Vesolje()
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)

    def _mapiraj(self, x: float, y: float) -> tuple[int]:
        return int(self.width * x), int(self.height * y)

    # TODO: DODANO ZARADI VIDNOSTI CELOTNE LADJE TUDI V SKRAJNI DESNI POZICIJI
    def omejitev_pozicije(self):
        if self.vesolje.ladja.x >= 0.9:
            self.vesolje.ladja.x = 0.9

    def narisi(self):
        # relativna velikost ladje

        vl_x, vl_y = self._mapiraj(x=self.vesolje.ladja.velikost_x, y=self.vesolje.ladja.velikost_y)
        v_x, v_y = self._mapiraj(x=self.vesolje.ladja.x, y=self.vesolje.ladja.y)
        pygame.display.set_caption("Space Invaders")
        # zapolni display z barvo, bela
        self.windowSurface.fill((0, 0, 0))
        # Spremeni velikost
        ladja = pygame.image.load("src/domain/ladja.png")

        velikost_ladje = pygame.transform.scale(ladja, (vl_x, vl_y))

        # nariši ladjo
        self.windowSurface.blit(velikost_ladje, (v_x, v_y - vl_y))
        pygame.display.update()

    def vnos(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vesolje.ladja.levo()
            self.vesolje.omejitev_ladje()

        elif keys[pygame.K_d]:
            self.vesolje.ladja.desno()
            self.vesolje.omejitev_ladje()
            self.omejitev_pozicije()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        pygame.display.update()
        self.clock.tick(1000)

    def konec(self):
        pass
