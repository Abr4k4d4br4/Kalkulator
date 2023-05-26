import cmath

class Kalkulator:
    def oblicz_pierwiastki(self, a, b, c): # obliczenie pierwiastków funkcji  z parametrów a, b, c równania
        delta = (b ** 2) - (4 * a * c)
        pierwiastek_delta = cmath.sqrt(delta)

        x1 = (-b - pierwiastek_delta) / (2 * a)
        x2 = (-b + pierwiastek_delta) / (2 * a)

        return x1, x2

