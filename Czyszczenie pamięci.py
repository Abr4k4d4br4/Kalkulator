class Kalkulator:
    def __init__(self):
        self.pamiec = 0
    
    def dodaj(self, x):
        self.pamiec += x
    
    def odejmij(self, x):
        self.pamiec -= x
    
    def pomnoz(self, x):
        self.pamiec *= x
    
    def podziel(self, x):
        self.pamiec /= x
    
    def wyczysc_pamiec(self):
        self.pamiec = 0
