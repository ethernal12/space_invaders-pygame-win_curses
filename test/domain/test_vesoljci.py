import unittest

from src.domain.vesoljec import Vesoljec


class Test_Vesoljci(unittest.TestCase):
    def setUp(self) -> None:
        self.x = 0.1
        self.y = 0.1
        self.velikost_x = 0.08
        self.velikost_y = 0.08
        self.hitrost = 0.02
        self.vesoljci = Vesoljec(x=self.x,
                                 y=self.y,
                                 velikost_x=self.velikost_x,
                                 velikost_y=self.velikost_y,
                                 hitrost=self.hitrost,

                                 )

    def test_init__(self):
        self.assertEqual(self.vesoljci.x, self.x)
        self.assertEqual(self.vesoljci.y, self.y)
        self.assertEqual(self.vesoljci.velikost_x, self.velikost_x)
        self.assertEqual(self.vesoljci.velikost_y, self.velikost_y)
        self.assertEqual(self.vesoljci.hitrost, self.hitrost)

    def test_premikanje(self):
        # premikanje levo
        self.vesoljci.x = 0.5
        x_vesoljca_pred = self.vesoljci.x
        self.vesoljci.premikanje()
        x_vesoljca_po = self.vesoljci.x
        self.assertTrue(x_vesoljca_pred < x_vesoljca_po)

        # premikanje desno
        x_vesoljca_pred = self.vesoljci.x
        self.vesoljci.x = 0
        self.vesoljci.premikanje()
        x_vesoljca_po = self.vesoljci.x
        self.assertTrue(x_vesoljca_pred > x_vesoljca_po)
