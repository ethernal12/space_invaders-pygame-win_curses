import unittest

from src.domain.bataljon import Bataljon
from src.domain.ladja import Ladja
from src.domain.vesolje import Vesolje


class Test_Vesolje(unittest.TestCase):
    def setUp(self) -> None:
        self.vesolje = Vesolje()

    def test___init__(self):
        self.assertTrue(isinstance(self.vesolje.ladja, Ladja))
        self.assertTrue(isinstance(self.vesolje.bataljon, Bataljon))
        self.assertTrue(isinstance(self.vesolje, Vesolje))

    def test_spremeni(self):
        # test bataljon menjava strani


        self.vesolje.ladja.x = 1.1

        self.assertEqual(self.vesolje.ladja.x, 1.1)

        self.vesolje.spremeni()
        print(self.vesolje.ladja.x)
        self.assertEqual(self.vesolje.ladja.x, 1 - self.vesolje.ladja.sirina / 2)

        self.vesolje.ladja.x = -0.1

        self.assertEqual(self.vesolje.ladja.x, -0.1)

        self.vesolje.spremeni()

        self.assertEqual(self.vesolje.ladja.x, 0 + self.vesolje.ladja.sirina / 2)

    def test_konec(self):
        pass


