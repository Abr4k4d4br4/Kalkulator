import unittest

from pierwiastki import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pierwiastki(self):
        a = 1
        b = -5
        c = 6

        x1, x2 = self.kalkulator.oblicz_pierwiastki(a, b, c)

        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, 3)

if __name__ == '__main__':
    unittest.main()