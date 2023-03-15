import unittest

from src.domain.vesoljci import Vesoljci


class Test_Vesoljci(unittest.TestCase):
    def setUp(self) -> None:
        self.x = 10
        self.y = 12
        self.velikost_x = 0.08
        self.velikost_y = 0.08
        self.hitrost = 0.02
        self.smer = 'desno'
        self.vesoljci = Vesoljci(x=self.x,
                                 y=self.y,
                                 velikost_x=self.velikost_x,
                                 velikost_y=self.velikost_y,
                                 hitrost=self.hitrost,
                                 smer=self.smer

                                 )

    def test_init__(self):
        self.assertEqual(self.vesoljci.x, self.x)
        self.assertEqual(self.vesoljci.y, self.y)
        self.assertEqual(self.vesoljci.velikost_x, self.velikost_x)
        self.assertEqual(self.vesoljci.velikost_y, self.velikost_y)
        self.assertEqual(self.vesoljci.hitrost, self.hitrost)
        self.assertEqual(self.vesoljci.smer, self.smer)

