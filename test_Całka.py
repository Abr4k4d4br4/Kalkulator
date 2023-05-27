#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from Całka import *



class MyTestCase(unittest.TestCase):
    def test_calka(self):
        self.assertEqual(1.9999999999999996, Kalkulator().calka(lambda x: x+2,-2,0,1000))


if __name__ == '__main__':
    unittest.main()


