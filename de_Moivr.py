#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def de_moivre(self, z, n): # zastosowanie wzoru de moivre dla liczb zespolonych
        modul = abs(z)
        argument = math.atan2(z.imag, z.real)
        nowy_modul = modul ** n
        nowy_argument = argument * n
        rzeczywista = nowy_modul * math.cos(nowy_argument)
        urojona = nowy_modul * math.sin(nowy_argument)
        self.memory.append(f"{z} ^ {n} = {complex(rzeczywista,urojona)}")
        self._trim_memory()
        return complex(rzeczywista, urojona)

