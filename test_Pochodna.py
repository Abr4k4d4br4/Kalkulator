#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from Pochodna import *


class MyTestCase(unittest.TestCase):
    def test_Pochodna(self):
        self.assertEqual(6.000100000012054, Kalkulator().pochodna(lambda x : x**2, 3))


if __name__ == '__main__':
    unittest.main()
