from dataclasses import dataclass

from src.domain.objekt import Objekt


@dataclass
class Ladja(Objekt):
	hitrost: float = 0.01

	def levo(self):
		self.x -= self.hitrost

	def desno(self):
		self.x += self.hitrost
