import random

from src.app._app import App
import sys
import pygame

from src.app.gui_config import GuiConfig
from src.domain.objekt import Objekt
from src.domain.strel import Strel
from src.domain.vesolje import Vesolje
from src.utils import pot
from src.settings import config as S


class Gui(App, GuiConfig):

    def __init__(self):
        super(Gui, self).__init__()
        self.vesolje = None
        self.flag = False
        self.shot_timer = 0

    def init(self):
        self.vesolje = Vesolje()

    def _mapiraj_obj(self, o: Objekt) -> tuple[int]:
        return *self._mapiraj(o.x - o.sirina / 2, o.y - o.visina / 2), *self._mapiraj(o.sirina, o.visina)

    def _mapiraj(self, x: float, y: float) -> tuple[int]:
        return int(self.sirina * x), int(self.visina * y)

    def narisi(self):
        if self.menu.is_enabled():
            self.menu.draw(self.surface)

        else:
            # ZAPOLNI DISPLAY Z BARVO, ČRNA
            self.surface.fill(S.APP.barve.bela)

            # MAPIRANJE POZICIJE IN VELIKOSTI LADJE
            l_x, l_y, vl_x, vl_y = self._mapiraj_obj(o=self.vesolje.ladja)

            # SPREMENI VELIKOST LADJE
            ladja = pygame.image.load(pot.media(S.APP.slike.ladja))

            velikost_ladje = pygame.transform.scale(ladja, (vl_x, vl_y))

            # NARIŠI LADJO
            self.surface.blit(velikost_ladje, (l_x, l_y))
            # TODO: PREMAKNI LOGIKO V VESOLJE ??
            for strel in self.vesolje.streli_ladja:
                s_x, s_y, sv_x, sv_y = self._mapiraj_obj(o=strel)

                strel_ladja = pygame.image.load(pot.media(S.APP.slike.strel_ladja))

                self.surface.blit(strel_ladja, (s_x + sv_x // 2, s_y - sv_y // 2))
                strel.premik_navzgor()
                if strel.y < 0:
                    self.vesolje.streli_ladja.remove(strel)
            # STREL VESOLJCI
            for strel in self.vesolje.streli_vesoljci:
                strel_vesoljci = pygame.image.load(pot.media(S.APP.slike.strel_vesoljec))
                s_x, s_y = self._mapiraj(x=strel.x, y=strel.y)
                self.surface.blit(strel_vesoljci, (s_x, s_y))
                strel.premakni_navzdol()
            self.shot_timer += 1

            if self.shot_timer >= 100:
                self.shot_timer = 0
                ran = random.randint(0, 8)
                nov_strel = Strel(x=self.vesolje.bataljon.vesoljci[ran].x, y=self.vesolje.bataljon.vesoljci[ran].y,
                                  sirina=0.1, visina=0.1,
                                  hitrost=0.01)
                self.vesolje.streli_vesoljci.append(nov_strel)
            # MAPIRANJE IN RISANJE VESOLJCEV
            vesoljci_slika = pygame.image.load(pot.media(S.APP.slike.vesoljci))
            for vesolc in self.vesolje.bataljon.vesoljci:
                v_x, v_y, vv_x, vv_y = self._mapiraj_obj(o=vesolc)
                velikost_vesoljcev = pygame.transform.scale(vesoljci_slika, (vv_x, vv_y))
                self.surface.blit(velikost_vesoljcev, (v_x, v_y + vv_y / 2))
        pygame.display.update()

    def pocakaj(self):
        self.vesolje.kontakt_vesoljc()
        if not self.menu.is_enabled():
            self.vesolje.spremeni()

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
                elif event.key == pygame.K_f:
                    novi_strel = Strel(x=self.vesolje.ladja.x, y=self.vesolje.ladja.y, sirina=0.1, visina=0.1,
                                       hitrost=0.02)
                    self.vesolje.streli_ladja.append(novi_strel)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vesolje.ladja.levo()

        elif keys[pygame.K_d]:
            self.vesolje.ladja.desno()
        pygame.display.update()
        self.clock.tick(S.APP.nastavitve.clock_tick)

    def konec(self) -> bool:
        return self.vesolje.konec()
