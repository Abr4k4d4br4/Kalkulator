#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]


    def potegowanie_macierzy(self,a, n): # potegownaie macierzy
        if n < 0:
            self.memory.append(f"Nie można obliczyć macierzy do potęgi {n}")
            self._trim_memory()
            return "Potęga musi być liczbą nieujemną."


        if n == 0:
            return Kalkulator().macierz_jednostkowa(len(a))

        result = a
        for _ in range(1, n):
            result = Kalkulator().mnozenie_macierzy(result, a)
        self.memory.append(f"{a} ^ {n} = {result}")
        self._trim_memory()
        return result