from dataclasses import dataclass

from src.domain.objekt import Objekt


@dataclass
class Strel(Objekt):
	hitrost: float

	def premikanje(self):
		self.y += self.hitrost
