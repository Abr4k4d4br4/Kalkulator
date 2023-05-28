#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from de_Moivr import *

class MyTestCase(unittest.TestCase):
    def test_de_Moivr(self):
        self.assertAlmostEqual((2j), Kalkulator().de_moivre((1+1j),2))


if __name__ == '__main__':
    unittest.main()
