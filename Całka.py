#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def calka(self, f, x1, x2, n = 1000): # f - funkcja, x1 - lewa granica, x2 - prawa granica, n - liczba trapezów (im więcej tym lepiej)
        sum = 0

        dx = (x2 - x1) / n

        for i in range(n):
            fx1 = x1 + dx * i
            fx2 = x1 + dx * (i + 1)

            sum += (f(fx1) + f(fx2)) / 2 * dx
        return sum


