import unittest

from src.domain.bataljon import Bataljon
from src.domain.ladja import Ladja
from src.domain.vesolje import Vesolje
from src.domain.vesoljec import Vesoljec


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
        self.assertEqual(self.vesolje.ladja.x, 1 - self.vesolje.ladja.sirina / 2)

        self.vesolje.ladja.x = -0.1

        self.assertEqual(self.vesolje.ladja.x, -0.1)

        self.vesolje.spremeni()

        self.assertEqual(self.vesolje.ladja.x, self.vesolje.ladja.sirina / 2)

    def test_konec(self):
        # testiraj nadaljevanje igre
        self.vesolje.bataljon.vesoljci = [Vesoljec(y=0.2, x=0, sirina=0.1, visina=0.1, hitrost=0.1),
                                          Vesoljec(y=0.3, x=0.1, sirina=0.1, visina=0.2, hitrost=0.1),
                                          Vesoljec(y=0.9, x=0.2, sirina=0.1, visina=0.1, hitrost=0.1)]
        self.assertEqual(self.vesolje.konec(), False)
        # testiraj konec igre
        self.vesolje.bataljon.vesoljci = [Vesoljec(y=0.2, x=0, sirina=0.1, visina=0.1, hitrost=0.1),
                                          Vesoljec(y=0.3, x=0.1, sirina=0.1, visina=0.2, hitrost=0.1),
                                          Vesoljec(y=1, x=0.2, sirina=0.1, visina=0.1, hitrost=0.1)]
        self.assertTrue(self.vesolje.konec())
