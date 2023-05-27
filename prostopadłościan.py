import math

class Kalkulator:
    def oblicz_pole_prostopadloscianu(self, dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c):
        return 2 * (dlugosc_boku_a * dlugosc_boku_b + dlugosc_boku_a * dlugosc_boku_c + dlugosc_boku_b * dlugosc_boku_c)

    def oblicz_objetosc_prostopadloscianu(self, dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c):
        return dlugosc_boku_a * dlugosc_boku_b * dlugosc_boku_c

