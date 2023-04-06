import random
from dataclasses import dataclass, field

from src.domain.bataljon import Bataljon
from src.domain.ladja import Ladja
from src.domain.objekt import Objekt
from src.domain.strel import Strel


@dataclass
class Vesolje:
	ladja: Ladja = None
	bataljon: Bataljon = None
	streli_ladja: list[Strel] = field(default_factory=list)
	streli_vesoljci: list[Strel] = field(default_factory=list)

	def __post_init__(self):
		self.ladja = Ladja(x=0.5, y=0.95, sirina=0.1, visina=0.1)
		self.bataljon = Bataljon(velikost=8)

	def spremeni(self):
		self.bataljon.premik()
		for strel in self.streli_ladja + self.streli_vesoljci:
			strel.premikanje()
		self._kontakt(self.bataljon.vesoljci, self.streli_ladja)
		if self.ladja.x + self.ladja.sirina / 2 > 1:
			self.ladja.x = 1 - self.ladja.sirina / 2
		elif self.ladja.x - self.ladja.sirina / 2 <= 0:
			self.ladja.x = 0 + self.ladja.sirina / 2

	def _kontakt(self, objekti: list[Objekt], streli: list[Strel]) -> bool:
		flag = False
		for strel in streli:
			for objekt in objekti:
				if objekt.dotik(strel):
					flag = True
					objekti.remove(objekt)
					streli.remove(strel)
					break
		return flag

	def ustreli_ladja(self):
		novi_strel = Strel(x=self.ladja.x, y=self.ladja.y, sirina=0.001, visina=0.1, hitrost=-0.02)
		self.streli_ladja.append(novi_strel)

	def ustreli_vesoljec(self):
		ran = random.randint(0, len(self.bataljon.vesoljci) - 1)
		novi_strel = Strel(
			x=self.bataljon.vesoljci[ran].x,
			y=self.bataljon.vesoljci[ran].y,
			sirina=0.001, visina=0.1,
			hitrost=0.01)
		self.streli_vesoljci.append(novi_strel)

	def konec(self) -> bool:
		if self.bataljon.vesoljci:
			najnizji = self.bataljon.najnizji()
			if najnizji.y + najnizji.visina > 1:
				return True
		return self._kontakt([self.ladja], self.streli_vesoljci)
