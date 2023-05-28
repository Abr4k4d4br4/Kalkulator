#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def zespolona(self, x, y): #tworzenie liczby zespolonej, x - część rzeczywista, y - część urojona
        self.memory.append(complex(x,y))
        self._trim_memory()
        return complex(x, y)