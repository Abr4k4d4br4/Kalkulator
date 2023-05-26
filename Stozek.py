import math

class Kalkulator:
    def oblicz_pole_stozka(self, promien, wysokosc):
        pole_podstawy = math.pi * promien ** 2
        tworzaca = math.sqrt(promien ** 2 + wysokosc ** 2)
        pole_boczne = math.pi * promien * tworzaca
        pole_calkowite = pole_podstawy + pole_boczne
        return pole_calkowite

    def oblicz_objetosc_stozka(self, promien, wysokosc):
        return (1 / 3) * math.pi * promien ** 2 * wysokosc
