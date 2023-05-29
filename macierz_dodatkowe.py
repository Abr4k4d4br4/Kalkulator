#!/usr/bin/python
# -*- coding: utf-8 -*-


class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def podmacierz(self,a, i, j): # podmacierz
        return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]

    def dopelnienie_algebraiczne(self,a): # dopelnienie algebraiczne
        n = len(a)
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                minor = Kalkulator().wyznacznik_macierzy(Kalkulator().podmacierz(a, i, j))
                row.append((-1) ** (i + j) * minor)
            result.append(row)
        return result

    def macierz_jednostkowa(self,n): # wyznaczenie macierzy jednostkowej
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            result.append(row)
        return result