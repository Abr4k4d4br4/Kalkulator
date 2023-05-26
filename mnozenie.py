#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def mnozenie(self, a, b): #mnożenie a razy b
        self.memory.append(f"{a} * {b} = {a*b}")
        self._trim_memory()
        return a * b