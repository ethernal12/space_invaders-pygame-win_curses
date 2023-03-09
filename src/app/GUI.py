import pygame_menu.widgets.core

from src.app._app import App
import sys
import pygame
import pygame_menu

from src.domain.vesolje import Vesolje
from src.utils import pot
from src.settings import config as S


class GUI(App):

    def __init__(self):
        self.sirina = S.CONFIG.pygame.dimenzija.sirina
        self.visina = S.CONFIG.pygame.dimenzija.visina
        pygame.init()

        # NAJVEČJA DOVOLJENA RESOLUCIJA
        self.info = pygame.display.Info()
        self.surface = pygame.display.set_mode((self.sirina, self.visina), 0, 32)

        # IZBIRA BARVNE TEME ZA MENIJE
        self.theme = pygame_menu.themes.THEME_BLUE

        self.menu = pygame_menu.Menu(
            S.JEZIK.aplikacija.naslov,
            self.sirina,
            self.visina,
            theme=self.theme
        )

        self.config_menu = pygame_menu.Menu(
            S.JEZIK.meni.konfiguracija,
            S.CONFIG.pygame.dimenzija.sirina,
            S.CONFIG.pygame.dimenzija.visina,
            theme=self.theme
        )

        self.font = pygame.font.Font(
            S.APP.font.tip,
            S.APP.font.velikost
        )

        self.clock = pygame.time.Clock()

        self.vnesi_ime_label = None

        self.vesolje = None
        self.vesoljci = None

        self._init_meni()
        self._init_config_meni()
        self.menu.enable()

    def _init_meni(self):
        # INICIALIZACIJA GLAVNEGA MENIJA
        self.vnesi_ime_label = self.menu.add.label(S.JEZIK.meni.vnesi_ime, background_color=S.APP.barve.bela)
        self.ime_igralca = self.menu.add.text_input(S.JEZIK.meni.ime,
                                                    onreturn=lambda ime: self._nastavi_ime(ime=ime))
        self.menu.add.button(S.JEZIK.meni.igraj, self._zazeni_igro)
        self.menu.add.button(S.JEZIK.meni.konfiguracija, self.config_menu)
        self.menu.add.button(S.JEZIK.meni.izhod, pygame_menu.events.EXIT)

    def _init_config_meni(self):
        # VELIKOSTI ZASLONA
        velikosti = [(S.JEZIK.meni_konfiguracija.zaslon.fullscreen, [self.info.current_w, self.info.current_h])]

        for dim in S.CONFIG.pygame.dimenzije:
            velikosti.append((f"{dim.sirina} x {dim.visina}", [dim.sirina, dim.visina]))
        # IZBIRA JEZIKA
        jeziki = []
        for izbira in S.CONFIG.pygame.izbira_jezika:
            jeziki.append((izbira.jezik, [izbira.jezik]))

        self.config_menu.add.dropselect(S.JEZIK.meni_konfiguracija.zaslon.velikost, items=velikosti,
                                        onchange=lambda _, velikost: self._nastavi_zaslon(velikost))
        self.config_menu.add.dropselect(S.JEZIK.meni_konfiguracija.jezik, items=jeziki,
                                        onchange=lambda _, tip: self._nastavi_jezik(tip))
        self.config_menu.add.button(S.JEZIK.nazaj, pygame_menu.events.BACK)

    def init(self):
        self.vesolje = Vesolje()
        self._narisi_vesoljce()

    def _mapiraj(self, x: float, y: float) -> tuple[int]:
        return int(self.sirina * x), int(self.visina * y)

    def _omejitev_pozicije_ladje(self):
        sirina = 1 - self.vesolje.ladja.velikost_x
        if self.vesolje.ladja.x >= sirina:
            self.vesolje.ladja.x = sirina

    def _omejitev_pozicije_vesoljcev(self):
        sirina = 1 - self.vesolje.vesoljci.velikost_x
        if self.vesolje.vesoljci.x >= sirina:
            self.vesolje.vesoljci.smer = "levo"

    def narisi(self):
        if self.menu.is_enabled():
            self.menu.draw(self.surface)

        else:
            # MAPIRANJE POZICIJE IN VELIKOSTI LADJE
            vl_x, vl_y = self._mapiraj(x=self.vesolje.ladja.velikost_x, y=self.vesolje.ladja.velikost_y)
            v_x, v_y = self._mapiraj(x=self.vesolje.ladja.x, y=self.vesolje.ladja.y)

            pygame.display.set_caption(S.JEZIK.aplikacija.naslov)
            # ZAPOLNI DISPLAY Z BARVO, ČRNA
            self.surface.fill(S.APP.barve.bela)
            # SPREMENI VELIKOST
            ladja = pygame.image.load(pot.data("media", "ladja.png"))

            velikost_ladje = pygame.transform.scale(ladja, (vl_x, vl_y))

            # PREMIKANJE VESOLJCEV

            # NARIŠI LADJO
            self.surface.blit(velikost_ladje, (v_x, v_y - vl_y))

            for i in range(len(self.vesolje.stev_vesoljcev)):
                # MAPIRANJE POZICIJE IN VELIKOSTI VEOSLJCEV
                vv_x, vv_y = self._mapiraj(x=self.vesolje.stev_vesoljcev[i].velikost_x, y=self.vesolje.stev_vesoljcev[i].velikost_y)
                ve_x, ve_y = self._mapiraj(x=self.vesolje.stev_vesoljcev[i].x, y=self.vesolje.stev_vesoljcev[i].y)
                # NARIŠI VESOLJCE
                vesoljci = pygame.image.load(pot.data("media", "vesoljci.png"))
                velikost_vesoljcev = pygame.transform.scale(vesoljci, (vv_x, vv_y))
                self.surface.blit(velikost_vesoljcev, (ve_x, ve_y + vv_y))
                self.vesolje.menjava_smeri_vesoljcev()
                self._omejitev_pozicije_vesoljcev()
                self.vesolje.stev_vesoljcev[i].premikanje()

        pygame.display.update()

    def vnos(self):
        events = pygame.event.get()
        if self.menu.is_enabled():
            self.menu.update(events)
            return
        # SPREMLJAJ INPUTE V IGRI
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
            self._omejitev_pozicije_ladje()

        # PREVERI ČE JE PRITISNJEN KATERI GUMB NA MENIJU

        pygame.display.update()
        self.clock.tick(S.APP.nastavitve.clock_tick)

    def _narisi_vesoljce(self):
        pass

    def konec(self) -> None:
        pass

    def _izrisi_text(self, naslov: str, tekst: str, pozicija_x: int, pozicija_y: int):
        # USTVARI TEXT PODLAGO
        text_podlaga = self.font.render(f'{naslov} {tekst}', True, S.APP.barve.bela)
        # NARIŠI TEXT NA CANVAS
        self.surface.blit(text_podlaga, (pozicija_x, pozicija_y))

    def _zazeni_igro(self):
        self.menu.disable()

    def _nastavi_ime(self, ime: str):
        S.CONFIG.igralec.ime = ime
        S.save()
        self.ime_igralca.hide()
        self.vnesi_ime_label.hide()

    def _nastavi_zaslon(self, velikost_zaslona: list):
        S.CONFIG.pygame.dimenzija.sirina = velikost_zaslona[0]
        S.CONFIG.pygame.dimenzija.visina = velikost_zaslona[1]
        S.save()

    def _nastavi_jezik(self, jezik: list):
        S.CONFIG.jezik = jezik[0]
        S.save()
