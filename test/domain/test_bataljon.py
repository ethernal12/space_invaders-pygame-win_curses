import unittest
from typing import List

from src.domain.bataljon import Bataljon
from src.domain.vector2D import Vector2D
from src.domain.vesolje import Vesolje
from src.domain.vesoljec import Vesoljec


class Test_Bataljon(unittest.TestCase):
    def setUp(self) -> None:
        self.st_vrst = 2
        self.velikost = 8
        self.razmik_vesoljcev_x = 0.1
        self.razmik_vesoljcev_y = 0.2
        self.premik_vesoljca_navzdol = 0.08
        self.bataljon = Bataljon(
            velikost=self.velikost,
            razmik_vesoljcev=Vector2D(x=self.razmik_vesoljcev_x, y=self.razmik_vesoljcev_y),
            premik_vesoljca_navzdol=self.premik_vesoljca_navzdol
        )
        self.vesolje = Vesolje()

    def test___init__(self):
        self.assertEqual(self.bataljon.velikost, self.velikost)
        self.assertIsInstance(self.bataljon.razmik_vesoljcev, Vector2D)
        self.assertEqual(self.bataljon.razmik_vesoljcev, Vector2D(self.razmik_vesoljcev_x, self.razmik_vesoljcev_y))
        self.assertEqual(self.bataljon.razmik_vesoljcev.x, self.razmik_vesoljcev_x)
        self.assertEqual(self.bataljon.razmik_vesoljcev.y, self.razmik_vesoljcev_y)
        self.assertEqual(self.bataljon.premik_vesoljca_navzdol, self.premik_vesoljca_navzdol)
        self.assertIsInstance(self.bataljon.vesoljci, List)
        self.assertEqual(len(self.bataljon.vesoljci), 16)
        for vesoljec in self.bataljon.vesoljci:
            self.assertIsInstance(vesoljec, Vesoljec)

    def test_premik(self):
        # test spremeni smer v levo
        self.vesolje.bataljon.vesoljci = [Vesoljec(y=1, x=0.95, sirina=0.1, visina=0.1, hitrost=0.1)]
        self.vesolje.bataljon.premik()
        self.assertTrue(self.vesolje.bataljon.vesoljci[0].hitrost == -0.1)
        # test spremeni smer v desno
        self.vesolje.bataljon.vesoljci[0].x = 0
        self.vesolje.bataljon.vesoljci[0].hitrost = -0.1
        self.vesolje.bataljon.premik()
        self.assertTrue(self.vesolje.bataljon.vesoljci[0].hitrost == 0.1)
        # test spremeni smer na sredini
        self.vesolje.bataljon.vesoljci[0].x = 0.5
        self.vesolje.bataljon.vesoljci[0].hitrost = -0.1
        self.vesolje.bataljon.vesoljci = [Vesoljec(y=1, x=0.5, sirina=0.1, visina=0.1, hitrost=-0.1)]
        self.vesolje.bataljon.premik()
        self.assertTrue(self.vesolje.bataljon.vesoljci[0].hitrost == -0.1)

    def test_najnizji(self):
        self.vesolje.bataljon.vesoljci = []
        self.vesolje.bataljon.vesoljci = [Vesoljec(y=0.2, x=0, sirina=0.1, visina=0.1, hitrost=0.1),
                                          Vesoljec(y=0.3, x=0.1, sirina=0.1, visina=0.2, hitrost=0.1),
                                          Vesoljec(y=0.4, x=0.2, sirina=0.1, visina=0.3, hitrost=0.1)]
        najnizji = self.vesolje.bataljon.najnizji()
        self.assertEqual(najnizji.y, self.vesolje.bataljon.vesoljci[-1].y)
