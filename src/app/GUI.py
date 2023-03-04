import pygame_menu.widgets.core
from pygame import Cursor

from src.app._app import App
import sys
import pygame
import pygame_menu

from typing import Optional

from src.domain.vesolje import Vesolje
from src.utils import pot, config


class GUI(App):

    def __init__(self, width: int, height: int):
        # Define colors
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.menu = None
        self.config_menu = None
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
        self.font = pygame.font.Font(config.CONFIG.font_type, config.CONFIG.font_size)
        theme = pygame_menu.themes.THEME_BLUE
        if config.CONFIG.theme_color == 'THEME_BLUE':
            theme = pygame_menu.themes.THEME_BLUE
        elif config.CONFIG.theme_color == 'THEME_ORANGE':
            theme = pygame_menu.themes.THEME_ORANGE
        elif config.CONFIG.theme_color == 'THEME_DARK':
            theme = pygame_menu.themes.THEME_DARK
        # inicializacija configuracijskega menija
        self.config_menu = pygame_menu.Menu('Konfiguracija', self.width, self.height,
                                            theme=theme)
        self.config_menu.add.dropselect("Velikost zaslona ", items=[
            ('400x400', [400, 400]),
            ('600x600', [600, 600]),
            ('800x800', [800, 800])
        ], onchange=lambda _, vrednost: self.ponastavi_velikost(vrednost))

        self.config_menu.add.dropselect("Barva menija", items=[
            ('Blue', "THEME_BLUE"),
            ('Orange', "THEME_ORANGE"),
            ('Dark', 'THEME_DARK')
        ], onchange=lambda _, vrednost: self.ponastavi('theme_color', vrednost))
        self.config_menu.add.button('Nazaj', pygame_menu.events.BACK)
        # inicializacija glavnega menija
        self.menu = pygame_menu.Menu(config.CONFIG.naslov_igre, self.width, self.height,
                                     theme=theme)
        self.menu.add.text_input(config.CONFIG.meni_ime, default=config.CONFIG.default_ime)
        self.menu.add.button(config.CONFIG.meni_igraj, self.zazeni_igro)
        self.menu.add.button(config.CONFIG.meni_config, self.config_menu)
        self.menu.add.button(config.CONFIG.meni_izhod, pygame_menu.events.EXIT)
        self.menu.enable()

    def onselect(self, mouse, widget, menu):
        value, index = widget.get_value()
        print(f'Selected item value: {value}, index: {index}')

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
            pygame.display.set_caption(config.CONFIG.naslov_igre)
            # zapolni display z barvo, bela
            self.windowSurface.fill((0, 0, 0))
            # Spremeni velikost
            ladja = pygame.image.load(pot.data("media", "ladja.png"))

            velikost_ladje = pygame.transform.scale(ladja, (vl_x, vl_y))

            # nariši ladjo
            self.windowSurface.blit(velikost_ladje, (v_x, v_y - vl_y))
        pygame.display.update()

    def vnos(self):
        events = pygame.event.get()
        if self.menu.is_enabled():
            self.menu.update(events)
            return
        # spremljaj inpute v igri
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.menu.enable()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vesolje.ladja.levo()
            self.vesolje.omejitev_ladje()

        elif keys[pygame.K_d]:
            self.vesolje.ladja.desno()
            self.vesolje.omejitev_ladje()
            self._omejitev_pozicije()

        # preveri če je pritisnjen kateri gumb na meniju

        pygame.display.update()
        self.clock.tick(1000)

    def konec(self) -> None:
        pass

    def _izrisi_text(self, naslov, tekst, pozicija_x, pozicija_y):
        # Ustvari text podlago
        text_podlaga = self.font.render(f'{naslov} {str(tekst)}', True, (255, 255, 0))
        # Nariši text na canvas
        self.windowSurface.blit(text_podlaga, (pozicija_x, pozicija_y))

    def zazeni_igro(self):
        self.menu.disable()

    def ponastavi(self, atribut, vrednost):
        setattr(config.CONFIG, atribut, vrednost)
        config.save()

    def ponastavi_velikost(self, vrednost):
        config.CONFIG.gui_velikost[0]["gui_width"] = vrednost[0]
        config.CONFIG.gui_velikost[0]["gui_height"] = vrednost[1]
        config.save()
