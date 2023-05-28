#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from trygonometryczna import *

class MyTestCase(unittest.TestCase):
    def trygonometryczna(self):
        self.assertEqual("1.4142135623730951 * (cos(0.7853981633974484) + isin(0.7853981633974482))",
                         Kalkulator().trygonometryczna(1 + 1j))


if __name__ == '__main__':
    unittest.main()
