#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def cz_rzeczywista(self, z): # wyznaczenie części rzeczywistej liczby zespolonej
        self.memory.append(f"Część rzeczywista {z} = {z.real}")
        self._trim_memory()
        return z.real