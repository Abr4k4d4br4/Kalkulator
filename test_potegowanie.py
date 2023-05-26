#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from potegowanie import *

class MyTestCase(unittest.TestCase):
    def potegowanie(self):
        self.assertEqual(9, Kalkulator().potegowanie(3,2))


if __name__ == '__main__':
    unittest.main()
