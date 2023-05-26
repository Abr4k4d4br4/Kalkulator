import unittest

from Pola_objetosci import Kalkulator

class KalkulatorTest(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pole_stozka(self):
        promien = 4
        wysokosc = 6
        pole_stozka = self.kalkulator.oblicz_pole_stozka(promien, wysokosc)
        self.assertEqual(pole_stozka, 140.8828696505485)

    def test_oblicz_objetosc_stozka(self):
        promien = 4
        wysokosc = 6
        objetosc_stozka = self.kalkulator.oblicz_objetosc_stozka(promien, wysokosc)
        self.assertEqual(objetosc_stozka, 100.53096491487338)
