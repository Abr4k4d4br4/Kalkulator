#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from wyznacznik_macierzy import *

class MyTestCase(unittest.TestCase):
    def test_wyznacznik_macierzy(self):
        self.assertEqual(-2, Kalkulator().wyznacznik_macierzy([[1, 2], [3, 4]]))
        self.assertEqual("Macierz musi być kwadratowa, aby obliczyć wyznacznik.", Kalkulator().wyznacznik_macierzy(
            [[1, 2, 3], [4, 5, 6]]))


if __name__ == '__main__':
    unittest.main()
