#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from dodawanie_macierz import *

class MyTestCase(unittest.TestCase):
    def test_dodawanie_macierz(self):
        self.assertEqual([[6, 8], [10, 12]], Kalkulator().dodawanie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
        self.assertEqual("Nie można dodać macierzy o różnych rozmiarach.", Kalkulator().dodawanie_macierzy(
            [[1, 2], [3, 4]], [[5, 5, 9], [1, 3, 3]]))


if __name__ == '__main__':
    unittest.main()
