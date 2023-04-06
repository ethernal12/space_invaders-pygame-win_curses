import pygame
import pygame_menu
import pygame_menu.widgets.core

from src.settings import config as S


class GuiConfig():

	def __init__(self):
		self.sirina = S.CONFIG.pygame.dimenzija.sirina
		self.visina = S.CONFIG.pygame.dimenzija.visina
		pygame.init()

		# NAJVEČJA DOVOLJENA RESOLUCIJA
		self.info = pygame.display.Info()
		self.surface = pygame.display.set_mode((self.sirina, self.visina), 0, 32)

		# IZBIRA BARVNE TEME ZA MENIJE
		self.theme = pygame_menu.themes.THEME_SOLARIZED
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
