#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from czy_parzysta import *

class MyTestCase(unittest.TestCase):
    def czy_patrzysta(self):
        self.assertEqual("Liczba jest liczbą parzystą", Kalkulator().parzysta(4))
        self.assertEqual("Liczba nie jest liczbą parzystą", Kalkulator().parzysta(3))


if __name__ == '__main__':
    unittest.main()
