#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from pierwiastkowanie import *

class MyTestCase(unittest.TestCase):
    def pierwiastkowanie(self):
        self.assertEqual(4, Kalkulator().pierwiastkowanie(16))
        self.assertEqual("Liczba mniejsza od zera!", Kalkulator().pierwiastkowanie(-3))


if __name__ == '__main__':
    unittest.main()
