#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def silnia(self, n):  # obliczenie silnii z liczby całkowitej n
        if n < 0:
            return "liczba jest mniejsza od 0"
        if n == 0:
            return 1
        else:
            return n * Kalkulator.silnia(self, n-1)

