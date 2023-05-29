#!/usr/bin/python
# -*- coding: utf-8 -*-


class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def macierz_transponowana(self,a): # wyznaczenie macierzy transponowanej
        result = []
        for j in range(len(a[0])):
            row = []
            for i in range(len(a)):
                row.append(a[i][j])
            result.append(row)
        self.memory.append(f"Macierz transponowana macierzy {a} = {result}")
        self._trim_memory()
        return result