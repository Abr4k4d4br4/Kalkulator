#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def pierwiastkowanie(self, a): #pierwiastkowanie pierwiastek kwadratowy z a
        if a < 0:
            return "Liczba mniejsza od zera!"
        else:
            self.memory.append(f"√{a} = {math.sqrt(a)}")
            self._trim_memory()
            return math.sqrt(a)