#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from liczba_zespolona import *

class MyTestCase(unittest.TestCase):
    def liczba_zespolona(self):
        self.assertEqual(3+4j, Kalkulator().zespolona(3,4))


if __name__ == '__main__':
    unittest.main()
