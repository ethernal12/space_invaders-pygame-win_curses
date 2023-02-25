import unittest

from src.domain.ladja import Ladja
from src.domain.vesolje import Vesolje


class Test_Vesolje(unittest.TestCase):
    def setUp(self) -> None:
        self.vesolje = Vesolje()

    def test___init__(self):
        self.assertTrue(isinstance(self.vesolje.ladja, Ladja))
        self.assertIsNone(self.vesolje.vesoljci)

    def test_omejitev_ladje(self):
        self.vesolje.ladja.x = 1.1

        self.assertEqual(self.vesolje.ladja.x, 0)

        self.vesolje.omejitev_ladje()

        self.assertEqual(self.vesolje.ladja.x, 1)

        self.vesolje.ladja.x = -0.1

        self.assertEqual(self.vesolje.ladja.x, -0.1)

        self.vesolje.omejitev_ladje()

        self.assertEqual(self.vesolje.ladja.x, 0)
