from dataclasses import dataclass


@dataclass
class Objekt:
	x: float
	y: float
	sirina: float
	visina: float

	def dotik(self, objekt: "Objekt") -> bool:
		ogljisca = [
			(objekt.x - objekt.sirina / 2, objekt.y - objekt.visina / 2),
			(objekt.x + objekt.sirina / 2, objekt.y - objekt.visina / 2),
			(objekt.x - objekt.sirina / 2, objekt.y + objekt.visina / 2),
			(objekt.x + objekt.sirina / 2, objekt.y + objekt.visina / 2),
		]

		for x, y in ogljisca:
			if (self.x - self.sirina / 2 < x < self.x + self.sirina / 2) and (
					self.y - self.visina / 2 < y < self.y + self.visina / 2):
				return True

		return False