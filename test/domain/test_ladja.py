import unittest

from src.domain.ladja import Ladja


class Test_Ladja(unittest.TestCase):
    def setUp(self) -> None:
        self.ladja_x = 0.5
        self.ladja_y = 1
        self.ladja_sirina = 0.1
        self.ladja_visina = 0.2
        self.ladja_hitrost = 0.003
        self.ladja = Ladja(x=self.ladja_x, y=self.ladja_y, sirina=self.ladja_sirina,
                           visina=self.ladja_visina,
                           hitrost=self.ladja_hitrost)

    def test_init(self):
        self.assertEqual(self.ladja.x, self.ladja_x)
        self.assertEqual(self.ladja.y, self.ladja_y)
        self.assertEqual(self.ladja.sirina, self.ladja_sirina)
        self.assertEqual(self.ladja.visina, self.ladja_visina)
        self.assertEqual(self.ladja.hitrost, self.ladja_hitrost)

    def test_levo(self):
        self.assertEqual(self.ladja.x, self.ladja_x)
        stari_x = self.ladja.x
        self.ladja.levo()

        self.assertTrue(self.ladja.x < stari_x)

    def test_desno(self):
        self.assertEqual(self.ladja.x, self.ladja_x)
        stari_x = self.ladja.x
        self.ladja.desno()

        self.assertTrue(self.ladja.x > stari_x)
