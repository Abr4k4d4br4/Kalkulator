import unittest

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_dodaj(self):
        self.kalkulator.dodaj(5)
        self.assertEqual(self.kalkulator.pamiec, 5)

    def test_odejmij(self):
        self.kalkulator.odejmij(3)
        self.assertEqual(self.kalkulator.pamiec, -3)

    def test_pomnoz(self):
        self.kalkulator.pomnoz(2)
        self.assertEqual(self.kalkulator.pamiec, 0)

    def test_podziel(self):
        self.kalkulator.podziel(4)
        self.assertEqual(self.kalkulator.pamiec, 0)

    def test_wyczysc_pamiec(self):
        self.kalkulator.dodaj(5)
        self.kalkulator.wyczysc_pamiec()
        self.assertEqual(self.kalkulator.pamiec, 0)

if __name__ == '__main__':
    unittest.main()