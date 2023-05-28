#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def trygonometryczna(self, z):  # przedstawienie liczby zespolonej w postaci trygonometrycznej
        modul = math.sqrt((z.real) ** 2 + (z.imag) ** 2)
        x = math.acos(z.real / modul)
        y = math.asin(z.imag / modul)
        modul1 = str(modul)
        x1 = str(x)
        y1 = str(y)
        zt = modul1 + " * (cos(" + x1 + ") + isin(" + y1 + "))"
        self.memory.append(f"{z} w postaci trygonometrycznej = {zt}")
        self._trim_memory()
        return zt