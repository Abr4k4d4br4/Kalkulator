#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def wyznacznik_macierzy(self, a): #liczenie wyznacznika macierzy
        if len(a) != len(a[0]):
            self.memory.append(f"Macierz {a} nie ma wyznacznika")
            self._trim_memory()
            return "Macierz musi być kwadratowa, aby obliczyć wyznacznik."


        n = len(a)
        if n == 1:
            return a[0][0]
        elif n == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        else:
            det = 0
            for j in range(n):
                det += (-1) ** j * a[0][j] * Kalkulator().wyznacznik_macierzy(Kalkulator().podmacierz(a, 0, j))
            self.memory.append(f"det{a} = {det}")
            self._trim_memory()
            return det