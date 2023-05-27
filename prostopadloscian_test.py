import unittest

from Pola_objetosci import Kalkulator

class KalkulatorTest(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pole_prostopadloscianu(self):
        dlugosc_boku_a = 3
        dlugosc_boku_b = 4
        dlugosc_boku_c = 5
        pole_prostopadloscianu = self.kalkulator.oblicz_pole_prostopadloscianu(dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c)
        self.assertEqual(pole_prostopadloscianu, 94)

    def test_oblicz_objetosc_prostopadloscianu(self):
        dlugosc_boku_a = 3
        dlugosc_boku_b = 4
        dlugosc_boku_c = 5
        objetosc_prostopadloscianu = self.kalkulator.oblicz_objetosc_prostopadloscianu(dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c)
        self.assertEqual(objetosc_prostopadloscianu, 60)


if __name__ == '__main__':
    unittest.main()