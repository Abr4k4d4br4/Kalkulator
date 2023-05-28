#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def cz_urojona(self,z): # wyznaczenie części urojonej liczby zespolonej
        self.memory.append(f"Część urojona {z} = {z.imag}")
        self._trim_memory()
        return z.imag