#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from dodawanie import *

class MyTestCase(unittest.TestCase):
    def test_dzialania(self):
        self.assertEqual(10, Kalkulator().dodawanie(7,3))


if __name__ == '__main__':
    unittest.main()
