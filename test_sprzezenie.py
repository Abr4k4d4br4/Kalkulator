#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from sprzezenie import *

class MyTestCase(unittest.TestCase):
    def sprzezenie(self):
        self.assertEqual(3-5j, Kalkulator().sprzezenie(3+5j))


if __name__ == '__main__':
    unittest.main()
