import unittest

from src.domain.ladja import Ladja


class Test_Ladja(unittest.TestCase):
    def setUp(self) -> None:
        self.ladja_x = 0.5
        self.ladja_y = 1
        self.ladja_velikost_x = 0.1
        self.ladja_velikost_y = 0.2
        self.ladja_hitrost = 0.003
        self.ladja = Ladja(x=self.ladja_x, y=self.ladja_y, velikost_x=self.ladja_velikost_x,
                           velikost_y=self.ladja_velikost_y,
                           hitrost=self.ladja_hitrost)

    def test_init(self):
        self.assertEqual(self.ladja.x, self.ladja_x)
        self.assertEqual(self.ladja.y, self.ladja_y)
        self.assertEqual(self.ladja.velikost_x, self.ladja_velikost_x)
        self.assertEqual(self.ladja.velikost_y, self.ladja_velikost_y)
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
