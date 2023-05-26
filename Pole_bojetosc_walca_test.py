import unittest

from Pole_objetosc_walca import Kalkulator

class KalkulatorTest(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pole_walca(self):
        promien = 3
        wysokosc = 5
        pole_walca = self.kalkulator.oblicz_pole_walca(promien, wysokosc)
        self.assertEqual(pole_walca, 150.79644737231007)

    def test_oblicz_objetosc_walca(self):
        promien = 3
        wysokosc = 5
        objetosc_walca = self.kalkulator.oblicz_objetosc_walca(promien, wysokosc)
        self.assertEqual(objetosc_walca, 141.3716694115407)