#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def sprzezenie(self, z): # tworzenie sprzężenia liczby zespolonej
        x = complex(z.real, -z.imag)
        self.memory.append(f"Sprzężenie {z} = {x}")
        self._trim_memory()
        return x