#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def parzysta(self, n): # sprawdzenie czy liczba n jest liczbą parzystą
        if n % 2 == 0:
            self.memory.append(f"Liczba {n} jest liczbą parzystą")
            self._trim_memory()
            return "Liczba jest liczbą parzystą"
        else:
            self.memory.append(f"Liczba {n} nie jest liczbą parzystą")
            self._trim_memory()
            return "Liczba nie jest liczbą parzystą"