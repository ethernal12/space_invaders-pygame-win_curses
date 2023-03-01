import pygame_menu.widgets.core

from src.app._app import App
import sys
import pygame
import pygame_menu

from typing import Optional

from src.domain.vesolje import Vesolje


class GUI(App):

    def __init__(self, width: int, height: int):
        self.menu = None
        self.width = width
        self.height = height
        self.windowSurface: Optional[pygame.Surface] = None
        self.clock = pygame.time.Clock()
        self.ladja = None
        self.font = None
        self.vesolje = None

    def init(self):
        pygame.init()
        self.vesolje = Vesolje()
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.menu = pygame_menu.Menu('Space Invaders - The Game', self.width, self.height,
                                     theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.text_input('Name :', default='John Doe')
        self.menu.add.button('Igraj', self.start_the_game)
        self.menu.add.button('Config', self.start_the_game)
        self.menu.add.button('Izhod', pygame_menu.events.EXIT)
        self.menu.enable()

    def _mapiraj(self, x: float, y: float) -> tuple[int]:
        return int(self.width * x), int(self.height * y)

    # TODO: DODANO ZARADI VIDNOSTI CELOTNE LADJE TUDI V SKRAJNI DESNI POZICIJI
    def _omejitev_pozicije(self):
        if self.vesolje.ladja.x >= 1 - self.vesolje.ladja.velikost_x:
            self.vesolje.ladja.x = 1 - self.vesolje.ladja.velikost_x

    def narisi(self):
        if self.menu.is_enabled():
            self.menu.draw(self.windowSurface)

        else:
            vl_x, vl_y = self._mapiraj(x=self.vesolje.ladja.velikost_x, y=self.vesolje.ladja.velikost_y)
            v_x, v_y = self._mapiraj(x=self.vesolje.ladja.x, y=self.vesolje.ladja.y)
            pygame.display.set_caption("Space Invaders")
            # zapolni display z barvo, bela
            self.windowSurface.fill((0, 0, 0))
            # Spremeni velikost
            ladja = pygame.image.load("data/media/ladja.png")

            velikost_ladje = pygame.transform.scale(ladja, (vl_x, vl_y))

            # nariši ladjo
            self.windowSurface.blit(velikost_ladje, (v_x, v_y - vl_y))
        pygame.display.update()

    def vnos(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        if keys[pygame.K_a]:
            self.vesolje.ladja.levo()
            self.vesolje.omejitev_ladje()

        elif keys[pygame.K_d]:
            self.vesolje.ladja.desno()
            self.vesolje.omejitev_ladje()
            self._omejitev_pozicije()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.menu.enable()
        # preveri če je pritisnjen kateri gumb na meniju
        if self.menu.is_enabled():
            self.menu.update(events)
        pygame.display.update()
        self.clock.tick(1000)

    def konec(self) -> None:
        pass

    def _izrisi_text(self, naslov, tekst, pozicija_x, pozicija_y):
        # Ustvari text podlago
        text_podlaga = self.font.render(f'{naslov} {str(tekst)}', True, (255, 255, 0))
        # Nariši text na canvas
        self.windowSurface.blit(text_podlaga, (pozicija_x, pozicija_y))

    def start_the_game(self):
        print('start the game')
        self.menu.disable()
