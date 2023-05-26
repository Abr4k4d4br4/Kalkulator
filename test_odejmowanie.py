#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from odejmowanie import *


class MyTestCase(unittest.TestCase):
    def odejmowanie(self):
        self.assertEqual(-5, Kalkulator().odejmowanie(4,9))


if __name__ == '__main__':
    unittest.main()
