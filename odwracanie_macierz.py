#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def odwracanie_macierzy(self,a): #wyznaczenie macierzy odwrotnej
        if len(a) != len(a[0]):
            self.memory.append(f"Macierz {a} nie ma odwrotności")
            self._trim_memory()
            return "Macierz musi być kwadratowa, aby mieć odwrotność."


        n = len(a)
        det = Kalkulator().wyznacznik_macierzy(a)
        if det == 0:
            self.memory.append(f"Macierz {a} nie ma odwrotności")
            self._trim_memory()
            return "Macierz nie ma odwrotności."


        adjugate = Kalkulator().macierz_transponowana(Kalkulator().dopelnienie_algebraiczne(a))
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(adjugate[i][j] / det)
            result.append(row)
        self.memory.append(f"Odwrotność macierzy {a} = {result}")
        self._trim_memory()
        return result