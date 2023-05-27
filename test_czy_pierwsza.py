#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from czy_pierwsza import *

class MyTestCase(unittest.TestCase):
    def czy_pierwsza(self):
        self.assertEqual("Liczba nie jest liczbą pierwszą", Kalkulator().czy_pierwsza(1))
        self.assertEqual("Liczba nie jest liczbą pierwszą", Kalkulator().czy_pierwsza(8))
        self.assertEqual("Liczba jest liczbą pierwszą", Kalkulator().czy_pierwsza(3))


if __name__ == '__main__':
    unittest.main()
