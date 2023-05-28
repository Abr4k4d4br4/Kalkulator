#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from wykladnicza import *


class MyTestCase(unittest.TestCase):
    def test_wykladnicza(self):
        self.assertEqual("1.4142135623730951 * e^i0.7853981633974483", Kalkulator().wykładnicza(1+1j))


if __name__ == '__main__':
    unittest.main()
