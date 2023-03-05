import os

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
        self.width = width
        self.height = height
        self.menu = None
        self.config_menu = None
        self.windowSurface: Optional[pygame.Surface] = None
        self.clock = pygame.time.Clock()
        self.ladja = None
        self.font = None
        self.vesolje = None
        self.info = None
        self.ime_igralca = None
        self.opozorilo = None

    def init(self):
        pygame.init()
        self.info = pygame.display.Info()
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
            ('700x700', [700, 700]),
            ('full screen', [self.info.current_w, self.info.current_h])
        ], onchange=lambda _, velikost: self._nastavi_zaslon(velikost))

        self.config_menu.add.dropselect("Barva menija", items=[
            ('Blue', "THEME_BLUE"),
            ('Orange', "THEME_ORANGE"),
            ('Dark', 'THEME_DARK')
        ], onchange=lambda _, vrednost: self._ponastavi(atribut='theme_color', vrednost=vrednost))
        self.config_menu.add.button("Nazaj", pygame_menu.events.BACK)

        # inicializacija glavnega menija
        self.menu = pygame_menu.Menu(config.CONFIG.naslov_igre, self.width, self.height,
                                     theme=theme)
        self.opozorilo = self.menu.add.label("Vpiši svoje ime in pritisni enter:", font_size=20,
                                             font_color=(config.CONFIG.barve["crna"]),
                                             background_color=config.CONFIG.barve["bela"])
        self.ime_igralca = self.menu.add.text_input(config.CONFIG.meni_ime,
                                                    onreturn=lambda vrednost: self._nastavi_ime(atribut='ime_igralca',
                                                                                                vrednost=vrednost))
        self.menu.add.button(config.CONFIG.meni_igraj, self._zazeni_igro)
        self.menu.add.button(config.CONFIG.meni_config, self.config_menu)
        self.menu.add.button(config.CONFIG.meni_izhod, pygame_menu.events.EXIT)
        self.menu.enable()

    def _mapiraj(self, x: float, y: float) -> tuple[int]:
        return int(self.width * x), int(self.height * y)

    def _omejitev_pozicije(self):
        if self.vesolje.ladja.x >= 1 - config.CONFIG.velikost_ladje_x:
            self.vesolje.ladja.x = 1 - config.CONFIG.velikost_ladje_x

    def narisi(self):
        if self.menu.is_enabled():
            self.menu.draw(self.windowSurface)

        else:
            vl_x, vl_y = self._mapiraj(x=self.vesolje.ladja.velikost_x, y=self.vesolje.ladja.velikost_y)
            v_x, v_y = self._mapiraj(x=self.vesolje.ladja.x, y=self.vesolje.ladja.y)
            pygame.display.set_caption(config.CONFIG.naslov_igre)
            # zapolni display z barvo, črna
            self.windowSurface.fill(config.CONFIG.barve["crna"])
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

    def _izrisi_text(self, naslov: str, tekst: str, pozicija_x: int, pozicija_y: int):
        # Ustvari text podlago
        text_podlaga = self.font.render(f'{naslov} {tekst}', True, config.CONFIG.barve["bela"])
        # Nariši text na canvas
        self.windowSurface.blit(text_podlaga, (pozicija_x, pozicija_y))

    def _zazeni_igro(self):
        self.menu.disable()

    def _ponastavi(self, atribut: str, vrednost: int):
        setattr(config.CONFIG, atribut, vrednost)
        config.save()

    def _nastavi_ime(self, atribut: str, vrednost: int):
        setattr(config.CONFIG, atribut, vrednost)
        config.save()
        self.ime_igralca.hide()
        self.opozorilo.hide()

    def _nastavi_zaslon(self, zaslona: list):
        config.CONFIG.gui_velikost["gui_width"] = zaslona[0]
        config.CONFIG.gui_velikost["gui_height"] = zaslona[1]
        config.save()
