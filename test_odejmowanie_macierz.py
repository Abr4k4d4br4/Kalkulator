#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from odejmowanie_macierz import *

class MyTestCase(unittest.TestCase):
    def test_odejmowanie_macierz(self):
        self.assertEqual([[-4, -4], [-4, -4]], Kalkulator().odejmowanie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
        self.assertEqual("Nie można odjąć macierzy o różnych rozmiarach.", Kalkulator().odejmowanie_macierzy(
            [[1, 2], [3, 4]], [[5, 5, 9], [1]]))


if __name__ == '__main__':
    unittest.main()
