import unittest

from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):

    def test_pole_kwadrat(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_kwadrat(4), 16)
        self.assertEqual(kalkulator.pole_kwadrat(0), 0)
        self.assertEqual(kalkulator.pole_kwadrat(-3), 9)

    def test_pole_prostokat(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_prostokat(3, 4), 12)
        self.assertEqual(kalkulator.pole_prostokat(0, 5), 0)
        self.assertEqual(kalkulator.pole_prostokat(-2, 6), -12)

    def test_pole_trojkat(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_trojkat(5, 4), 10)
        self.assertEqual(kalkulator.pole_trojkat(0, 3), 0)
        self.assertEqual(kalkulator.pole_trojkat(-3, 2), -3)

    def test_pole_trapez(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_trapez(4, 5, 6), 27)
        self.assertEqual(kalkulator.pole_trapez(0, 2, 3), 3)
        self.assertEqual(kalkulator.pole_trapez(-3, 4, 5), -7.5)

    def test_pole_romb(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_romb(4, 5), 10)
        self.assertEqual(kalkulator.pole_romb(0, 2), 0)
        self.assertEqual(kalkulator.pole_romb(-3, 4), -6)

    def test_pole_rownoleglobok(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_rownoleglobok(3, 4), 12)
        self.assertEqual(kalkulator.pole_rownoleglobok(0, 5), 0)
        self.assertEqual(kalkulator.pole_rownoleglobok(-2, 6), -12)

    def test_pole_kola(self):
        kalkulator = Kalkulator()
        self.assertAlmostEqual(kalkulator.pole_kola(3), 28.26, places=2)
        self.assertAlmostEqual(kalkulator.pole_kola(0), 0, places=2)
        self.assertAlmostEqual(kalkulator.pole_kola(-2), 12.57, places=2)

    def test_pole_szesciokat(self):
        kalkulator = Kalkulator()
        self.assertAlmostEqual(kalkulator.pole_szesciokat(4), 41.57, places=2)
        self.assertAlmostEqual(kalkulator.pole_szesciokat(0), 0, places=2)
        self.assertAlmostEqual(kalkulator.pole_szesciokat(-3), 15.59, places=2)

    def test_pole_trojakt_rownoboczny(self):
        kalkulator = Kalkulator()
        self.assertAlmostEqual(kalkulator.pole_trojakt_rownoboczny(6, 4), 6.93, places=2)
        self.assertAlmostEqual(kalkulator.pole_trojakt_rownoboczny(0, 3), 0, places=2)
        self.assertAlmostEqual(kalkulator.pole_trojakt_rownoboczny(-3, 2), -1.04, places=2)

    def test_pole_trojakt_prostokatny(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_trojakt_prostokatny(3, 4), 6)
        self.assertEqual(kalkulator.pole_trojakt_prostokatny(0, 5), 0)
        self.assertEqual(kalkulator.pole_trojakt_prostokatny(-2, 6), -6)

    def test_pole_trojakt_kat(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_trojakt_kat(3, 4, 0.5), 3)
        self.assertEqual(kalkulator.pole_trojakt_kat(0, 5, 0.3), 0)
        self.assertEqual(kalkulator.pole_trojakt_kat(-2, 6, 0.7), -4.2)

    def test_pole_romb_znak(self):
        kalkulator = Kalkulator()
        self.assertEqual(kalkulator.pole_romb_znak(4, 5), 10)
        self.assertEqual(kalkulator.pole_romb_znak(0, 2), 0)
        self.assertEqual(kalkulator.pole_romb_znak(-3, 4), -6)

if __name__ == '__main__':
    unittest.main()
