#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from mnozenie import *

class MyTestCase(unittest.TestCase):
    def mnozenie(self):
        self.assertEqual(18, Kalkulator().mnozenie(3,6))


if __name__ == '__main__':
    unittest.main()
