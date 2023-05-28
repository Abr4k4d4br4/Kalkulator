import unittest
import math

from liczba_e import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_potegowanie_liczby_e(self):
        result = self.kalkulator.oblicz_potegowanie_liczby_e(2)
        self.assertAlmostEqual(result, math.exp(2))

if __name__ == '__main__':
    unittest.main()
