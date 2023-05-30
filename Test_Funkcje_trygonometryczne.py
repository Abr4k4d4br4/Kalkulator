import unittest
import math

from your_module import Kalkulator

class KalkulatorTestCase(unittest.TestCase):

    def test_sin(self):
        self.assertEqual(Kalkulator.sinus(0), math.sin(0))
        self.assertEqual(Kalkulator.sinus(math.pi / 2), math.sin(math.pi / 2))
        self.assertEqual(Kalkulator.sinus(math.pi), math.sin(math.pi))

    def test_cos(self):
        self.assertEqual(Kalkulator.cosinus(0), math.cos(0))
        self.assertEqual(Kalkulator.cosinus(math.pi / 2), math.cos(math.pi / 2))
        self.assertEqual(Kalkulator.cosinus(math.pi), math.cos(math.pi))

    def test_tan(self):
        self.assertEqual(Kalkulator.tangens(0), math.tan(0))
        self.assertEqual(Kalkulator.tangens(math.pi / 4), math.tan(math.pi / 4))
        self.assertEqual(Kalkulator.tangens(math.pi / 2), math.tan(math.pi / 2))

    def test_cotan(self):
        self.assertEqual(Kalkulator.cotangens(0), 1 / math.tan(0))
        self.assertEqual(Kalkulator.cotangens(math.pi / 4), 1 / math.tan(math.pi / 4))
        self.assertEqual(Kalkulator.cotangens(math.pi / 2), 1 / math.tan(math.pi / 2))

    def test_arcsin(self):
        self.assertEqual(Kalkulator.arcsinus(0), math.asin(0))
        self.assertEqual(Kalkulator.arcsinus(0.5), math.asin(0.5))
        self.assertEqual(Kalkulator.arcsinus(1), math.asin(1))

    def test_arccos(self):
        self.assertEqual(Kalkulator.arccosinus(0), math.acos(0))
        self.assertEqual(Kalkulator.arccosinus(0.5), math.acos(0.5))
        self.assertEqual(Kalkulator.arccosinus(1), math.acos(1))

    def test_arctan(self):
        self.assertEqual(Kalkulator.arctangens(0), math.atan(0))
        self.assertEqual(Kalkulator.arctangens(1), math.atan(1))
        self.assertEqual(Kalkulator.arctangens(math.inf), math.atan(math.inf))

    def test_arccotan(self):
        self.assertEqual(Kalkulator.arccotangens(1), math.atan(1 / 1))
        self.assertEqual(Kalkulator.arccotangens(0.5), math.atan(1 / 0.5))
        self.assertEqual(Kalkulator.arccotangens(0), math.atan(1 / 0))

    def test_sinh(self):
        self.assertEqual(Kalkulator.sinh(0), math.sinh(0))
        self.assertEqual(Kalkulator.sinh(1), math.sinh(1))
        self.assertEqual(Kalkulator.sinh(math.inf), math.sinh(math.inf))

    def test_cosh(self):
        self.assertEqual(Kalkulator.cosh(0), math.cosh(0))
        self.assertEqual(Kalkulator.cosh(1), math.cosh(1))
        self.assertEqual(Kalkulator.cosh(math.inf), math.cosh(math.inf))

    def test_tanh(self):
        self.assertEqual(Kalkulator.tanh(0), math.tanh(0))
        self.assertEqual(Kalkulator.tanh(1), math.tanh(1))
        self.assertEqual(Kalkulator.tanh(math.inf), math.tanh(math.inf))

    def test_asinh(self):
        self.assertEqual(Kalkulator.asinh(0), math.asinh(0))
        self.assertEqual(Kalkulator.asinh(1), math.asinh(1))
        self.assertEqual(Kalkulator.asinh(math.inf), math.asinh(math.inf))

    def test_acosh(self):
        self.assertEqual(Kalkulator.acosh(1), math.acosh(1))
        self.assertEqual(Kalkulator.acosh(2), math.acosh(2))
        self.assertEqual(Kalkulator.acosh(math.inf), math.acosh(math.inf))

    def test_atanh(self):
        self.assertEqual(Kalkulator.atanh(0), math.atanh(0))
        self.assertEqual(Kalkulator.atanh(0.5), math.atanh(0.5))
        self.assertEqual(Kalkulator.atanh(1), math.atanh(1))

if __name__ == '__main__':
    unittest.main()
