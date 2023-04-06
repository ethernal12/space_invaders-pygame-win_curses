import sys

import pygame

from src.app._app import App
from src.app.gui_config import GuiConfig
from src.domain.objekt import Objekt
from src.domain.vesolje import Vesolje
from src.settings import config as S
from src.utils import pot


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

			# SPREMENI VELIKOST LADJE
			ladja = pygame.image.load(pot.media(S.APP.slike.ladja))
			l_x, l_y, vl_x, vl_y = self._mapiraj_obj(o=self.vesolje.ladja)
			velikost_ladje = pygame.transform.scale(ladja, (vl_x, vl_y))

			# NARIŠI LADJO
			strel_ladja = pygame.image.load(pot.media(S.APP.slike.strel_ladja))
			self.surface.blit(velikost_ladje, (l_x, l_y))
			for strel in self.vesolje.streli_ladja:
				s_x, s_y, sv_x, sv_y = self._mapiraj_obj(o=strel)
				pygame.transform.scale(strel_ladja, (sv_x, sv_y))
				self.surface.blit(strel_ladja, (s_x + sv_x // 2, s_y + sv_y // 2))

			# STREL VESOLJCI
			strel_vesoljci = pygame.image.load(pot.media(S.APP.slike.strel_vesoljec))
			for strel in self.vesolje.streli_vesoljci:
				s_x, s_y, sv_x, sv_y = self._mapiraj_obj(o=strel)
				pygame.transform.scale(strel_ladja, (5, 5))
				self.surface.blit(strel_vesoljci, (s_x + sv_x // 2, s_y + sv_y // 2))

			# MAPIRANJE IN RISANJE VESOLJCEV
			vesoljci_slika = pygame.image.load(pot.media(S.APP.slike.vesoljci))
			for vesolc in self.vesolje.bataljon.vesoljci:
				v_x, v_y, vv_x, vv_y = self._mapiraj_obj(o=vesolc)
				velikost_vesoljcev = pygame.transform.scale(vesoljci_slika, (vv_x, vv_y))
				self.surface.blit(velikost_vesoljcev, (v_x + vv_x // 2, v_y + vv_y // 2))
		pygame.display.update()

	def pocakaj(self):
		if not self.menu.is_enabled():
			self.vesolje.spremeni()

			self.shot_timer += 1
			if self.shot_timer >= 100:
				self.shot_timer = 0
				self.vesolje.ustreli_vesoljec()

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
					self.vesolje.ustreli_ladja()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.vesolje.ladja.levo()

		elif keys[pygame.K_d]:
			self.vesolje.ladja.desno()
		pygame.display.update()
		self.clock.tick(S.APP.nastavitve.clock_tick)

	def konec(self) -> bool:
		return self.vesolje.konec()
