#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from transponowanie_macierz import *

class MyTestCase(unittest.TestCase):
    def test_transponowanie_macierzy(self):
        self.assertEqual([[1,3], [2,4]], Kalkulator().macierz_transponowana([[1,2], [3,4]]))


if __name__ == '__main__':
    unittest.main()
