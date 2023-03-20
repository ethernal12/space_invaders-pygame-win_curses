import unittest

from src.domain.ladja import Ladja
from src.domain.vesolje import Vesolje


class Test_Vesolje(unittest.TestCase):
    def setUp(self) -> None:
        self.st_vrst = 2
        self.st_vesoljcev = 8
        self.razmik_vesoljcev_x = 10
        self.razmik_vesoljcev_y = 12
        self.premik_vesoljca_navzdol = 0.08
        self.velikost_vesoljca_x = 0.08
        self.velikost_vesoljca_y = 0.08
        self.vesolje = Vesolje(
            st_vesoljcev=self.st_vesoljcev,
            razmik_vesoljcev_x=self.razmik_vesoljcev_x,
            razmik_vesoljcev_y=self.razmik_vesoljcev_y,
            premik_vesoljca_navzdol=self.premik_vesoljca_navzdol,
            velikost_vesoljca_x=self.velikost_vesoljca_x,
            velikost_vesoljca_y=self.velikost_vesoljca_y
        )

    def test___init__(self):
        self.assertEqual(self.vesolje.st_vesoljcev, self.st_vesoljcev)
        self.assertEqual(self.vesolje.razmik_vesoljcev_x, self.razmik_vesoljcev_x)
        self.assertEqual(self.vesolje.razmik_vesoljcev_y, self.razmik_vesoljcev_y)
        self.assertEqual(self.vesolje.premik_vesoljca_navzdol, self.premik_vesoljca_navzdol)
        self.assertEqual(self.vesolje.velikost_vesoljca_x, self.velikost_vesoljca_x)
        self.assertEqual(self.vesolje.velikost_vesoljca_y, self.velikost_vesoljca_y)
        self.assertTrue(isinstance(self.vesolje.ladja, Ladja))
        self.assertTrue(isinstance(self.vesolje, Vesolje))
        self.assertEqual(len(self.vesolje.vesoljci), self.st_vrst * self.st_vesoljcev)

    def test_omejitev_ladje(self):
        self.vesolje.ladja.x = 1.1

        self.assertEqual(self.vesolje.ladja.x, 1.1)

        self.vesolje.omejitev_ladje()

        self.assertEqual(self.vesolje.ladja.x, 1)

        self.vesolje.ladja.x = -0.1

        self.assertEqual(self.vesolje.ladja.x, -0.1)

        self.vesolje.omejitev_ladje()

        self.assertEqual(self.vesolje.ladja.x, 0)

    def test_menjava_smeri_vesoljcev(self):
        self.vesolje.vesoljci[-1].x = 1
        self.vesolje.menjava_smeri_vesoljcev()

        for i in range(len(self.vesolje.vesoljci)):
            self.assertTrue(self.vesolje.vesoljci[i].hitrost < 0)

        self.vesolje.vesoljci[-1].x = 0
        self.vesolje.menjava_smeri_vesoljcev()
        for i in range(len(self.vesolje.vesoljci)):
            self.assertTrue(self.vesolje.vesoljci[i].hitrost > 0)
