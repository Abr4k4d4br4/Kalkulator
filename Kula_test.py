import unittest

from Pola_objetosci import Kalkulator

class KalkulatorTest(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pole_kuli(self):
        promien = 5
        pole_kuli = self.kalkulator.oblicz_pole_kuli(promien)
        self.assertEqual(pole_kuli, 314.1592653589793)


    def test_oblicz_objetosc_kuli(self):
        promien = 5
        objetosc_kuli = self.kalkulator.oblicz_objetosc_kuli(promien)
        self.assertEqual(objetosc_kuli, 523.5987755982989)
