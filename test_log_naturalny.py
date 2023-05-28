import unittest
import math

from liczba_e import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_logarytm_naturalny(self):
        result = self.kalkulator.oblicz_logarytm_naturalny(10)
        self.assertAlmostEqual(result, math.log(10))

if __name__ == '__main__':
    unittest.main()
