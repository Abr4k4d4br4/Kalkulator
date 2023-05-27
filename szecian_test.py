import unittest

from Pola_objetosci import Kalkulator

class KalkulatorTest(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pole_szescianu(self):
        dlugosc_boku = 4
        pole_szescianu = self.kalkulator.oblicz_pole_szescianu(dlugosc_boku)
        self.assertEqual(pole_szescianu, 96)

    def test_oblicz_objetosc_szescianu(self):
        dlugosc_boku = 4
        objetosc_szescianu = self.kalkulator.oblicz_objetosc_szescianu(dlugosc_boku)
        self.assertEqual(objetosc_szescianu, 64)

if __name__ == '__main__':
    unittest.main()