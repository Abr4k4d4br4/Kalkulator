#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def odejmowanie_macierzy(self,a, b): #odejmowanie macierzy
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            self.memory.append(f"Macierze {a} i {b} są róznych rozmiarów")
            self._trim_memory()
            return "Nie można odjąć macierzy o różnych rozmiarach."


        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[i])):
                row.append(a[i][j] - b[i][j])
            result.append(row)
        self.memory.append(f"{a} - {b} = {result}")
        self._trim_memory()
        return result