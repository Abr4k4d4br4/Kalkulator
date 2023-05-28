#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from cz_urojona import *

class MyTestCase(unittest.TestCase):
    def czesc_urojona(self):
        self.assertEqual(-8, Kalkulator().cz_urojona(6-8j))


if __name__ == '__main__':
    unittest.main()
