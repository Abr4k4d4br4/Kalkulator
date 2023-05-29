#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def mnozenie_macierzy(self,a, b): #mnożenie macierzy
        if len(a[0]) != len(b):
            self.memory.append(f"Nie można pomnożyć macierzy {a} i {b}")
            self._trim_memory()
            return "Nie można pomnożyć tych macierzy."


        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                sum = 0
                for k in range(len(b)):
                    sum += a[i][k] * b[k][j]
                row.append(sum)
            result.append(row)
        self.memory.append(f"{a} * {b} = {result}")
        self._trim_memory()
        return result