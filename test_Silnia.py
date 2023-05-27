#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from Silnia import *

class MyTestCase(unittest.TestCase):
    def test_silnia(self):
        self.assertEqual(6, Kalkulator().silnia(3))
        self.assertEqual(1, Kalkulator().silnia(0))
        self.assertEqual("liczba jest mniejsza od 0", Kalkulator().silnia(-3))


if __name__ == '__main__':
    unittest.main()
