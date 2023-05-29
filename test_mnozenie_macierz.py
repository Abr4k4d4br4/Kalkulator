#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from mnozenie_macierz import *

class MyTestCase(unittest.TestCase):
    def test_mnozenie_macierz(self):
        self.assertEqual([[19, 22], [43, 50]], Kalkulator().mnozenie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
        self.assertEqual("Nie można pomnożyć tych macierzy.", Kalkulator().mnozenie_macierzy(
            [[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]]))


if __name__ == '__main__':
    unittest.main()
