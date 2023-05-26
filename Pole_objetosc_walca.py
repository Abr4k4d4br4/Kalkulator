import math

class Kalkulator:
    def oblicz_pole_walca(self, promien, wysokosc):
        pole_podstawy = math.pi * promien ** 2
        pole_boczne = 2 * math.pi * promien * wysokosc
        pole_calkowite = 2 * pole_podstawy + pole_boczne
        return pole_calkowite


    def oblicz_objetosc_walca(self, promien, wysokosc):
        return math.pi * promien ** 2 * wysokosc
