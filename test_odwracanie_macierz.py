#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from odwracanie_macierz import *

class MyTestCase(unittest.TestCase):
    def test_odwracanie_macierz(self):
        self.assertEqual([[-2.0, 1.0], [1.5, -0.5]], Kalkulator().odwracanie_macierzy([[1, 2], [3, 4]]))
        self.assertEqual("Macierz musi być kwadratowa, aby mieć odwrotność.", Kalkulator().odwracanie_macierzy(
            [[1, 2], [3, 4], [5, 6]]))
        self.assertEqual("Macierz nie ma odwrotności.", Kalkulator().odwracanie_macierzy([[1, 1], [1, 1]]))


if __name__ == '__main__':
    unittest.main()
