#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def wykładnicza(self,z): # przedstawienie liczby zespolonej w postaci wykładniczej
        modul = abs(z)
        argument = math.atan2(z.imag, z.real)
        m1 = str(modul)
        arg = str(argument)
        zw = m1 + " * e^i" + arg
        self.memory.append(f"{z} w postaci wykładniczej = {zw}")
        self._trim_memory()
        return zw