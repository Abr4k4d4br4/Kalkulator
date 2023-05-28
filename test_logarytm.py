import unittest
import math

from liczba_e import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_logarytm(self):
        result = self.kalkulator.oblicz_logarytm(8, 2)
        self.assertAlmostEqual(result, math.log(8, 2))

if __name__ == '__main__':
    unittest.main()
