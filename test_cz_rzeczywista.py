#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from cz_rzeczywista import *

class MyTestCase(unittest.TestCase):
    def cz_rzeczywista(self):
        self.assertEqual(4, Kalkulator().cz_rzeczywista(4-7j))


if __name__ == '__main__':
    unittest.main()
