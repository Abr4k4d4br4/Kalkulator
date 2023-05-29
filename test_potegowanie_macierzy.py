#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from potega_macierz import *

class MyTestCase(unittest.TestCase):
    def test_potegowanie_macierzy(self):
        self.assertEqual([[37, 54], [81, 118]], Kalkulator().potegowanie_macierzy([[1, 2], [3, 4]], 3))
        self.assertEqual("Potęga musi być liczbą nieujemną.", Kalkulator().potegowanie_macierzy([[1, 2], [3, 4]], -1))


if __name__ == '__main__':
    unittest.main()
