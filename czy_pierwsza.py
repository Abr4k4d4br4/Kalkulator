#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def czy_pierwsza(self, n): # sprawdzanie czy liczba n jest liczbą pierwszą
        if n < 2:
            self.memory.append(f"Liczba {n} nie jest liczbą pierwszą")
            self._trim_memory()
            return "Liczba nie jest liczbą pierwszą"
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                self.memory.append(f"Liczba {n} nie jest liczbą pierwszą")
                self._trim_memory()
                return "Liczba nie jest liczbą pierwszą"

        self.memory.append(f"Liczba {n} jest liczbą pierwszą")
        self._trim_memory()
        return "Liczba jest liczbą pierwszą"