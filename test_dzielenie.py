#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from dzielenie import *

class MyTestCase(unittest.TestCase):
    def dzielenie(self):
        self.assertEqual(2, Kalkulator().dzielenie(18,9))
        self.assertEqual("Dzielenie przez zero!", Kalkulator().dzielenie(3, 0))


if __name__ == '__main__':
    unittest.main()
