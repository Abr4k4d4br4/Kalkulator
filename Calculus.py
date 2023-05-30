#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

e = math.e
pi = math.pi

class Kalkulator:
    def __init__(self):  # tworzenie pamięci
        self.memory = []

    def _trim_memory(self):  # pamieć ostatnich dziesięciu zadań
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def odwolaj_zadanie(self, index): # odwoływnaie się do zadania
        try:
            return self.memory[index]
        except IndexError:
            print("Podany indeks nie istnieje w pamięci.")

    def czyszczenie_pamieci(self): # czyszczenie pamięci
        self.memory = []

    # PODSTAWOWE DZIALANIA

    def dodawanie(self, a, b): #dodawanie a dodać b
        self.memory.append(f"{a} + {b} = {a+b}")
        self._trim_memory()
        return a + b

    def odejmowanie(self, a, b): #odejmowanie a odjąć b
        self.memory.append(f"{a} - {b} = {a-b}")
        self._trim_memory()
        return a - b

    def mnozenie(self, a, b): #mnożenie a razy b
        self.memory.append(f"{a} * {b} = {a*b}")
        self._trim_memory()
        return a * b

    def dzielenie(self, a, b): #dzielenie a przez b
        if b == 0:
            return "Dzielenie przez zero!"
        else:
            self.memory.append(f"{a} / {b} = {a/b}")
            self._trim_memory()
            return a/b

    def potegowanie(self, a, b): #potęgowanie a do potęgi b
        self.memory.append(f"{a} ^ {b} = {a**b}")
        self._trim_memory()
        return a**b

    def pierwiastkowanie(self, a): #pierwiastkowanie pierwiastek kwadratowy z a
        if a < 0:
            return "Liczba mniejsza od zera!"
        else:
            self.memory.append(f"√{a} = {math.sqrt(a)}")
            self._trim_memory()
            return math.sqrt(a)

    #CALKA

    def calka(self, f, x1, x2, n = 1000): # f - funkcja, x1 - lewa granica, x2 - prawa granica, n - liczba trapezów (im więcej tym lepiej)
        sum = 0

        dx = (x2 - x1) / n

        for i in range(n):
            fx1 = x1 + dx * i
            fx2 = x1 + dx * (i + 1)

            sum += (f(fx1) + f(fx2)) / 2 * dx

        self.memory.append(f"Calka z {f} w przedziale od {x1} do {x2} = {sum}")
        self._trim_memory()

        return sum

    # PARZYSTA

    def parzysta(self, n): # sprawdzenie czy liczba n jest liczbą parzystą
        if n % 2 == 0:
            self.memory.append(f"Liczba {n} jest liczbą parzystą")
            self._trim_memory()
            return "Liczba jest liczbą parzystą"
        else:
            self.memory.append(f"Liczba {n} nie jest liczbą parzystą")
            self._trim_memory()
            return "Liczba nie jest liczbą parzystą"

    # PIERWSZA

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

    # POCHODNA

    def pochodna(self, f, x, h=0.0001):   # f - funkcja, x - punkt w którym liczymy pochodną, h - skok
        self.memory.append(f"f'({x}) = {(f(x + h) - f(x)) / h}")
        self._trim_memory()
        return (f(x + h) - f(x)) / h

    # SILNIA

    def silnia(self, n):  # obliczenie silnii z liczby całkowitej n
        if n < 0:
            self.memory.append(f"Liczba {n} jest mniejsza od 0")
            self._trim_memory()
            return "liczba jest mniejsza od 0"
        s = 1
        for i in range(2, n + 1):
            s *= i

        self.memory.append(f"{n}! = {s}")
        self._trim_memory()
        return s

    #ZESPOLONE

    def zespolona(self, x, y): #tworzenie liczby zespolonej, x - część rzeczywista, y - część urojona
        self.memory.append(complex(x,y))
        self._trim_memory()
        return complex(x, y)

    def sprzezenie(self, z): # tworzenie sprzężenia liczby zespolonej
        x = complex(z.real, -z.imag)
        self.memory.append(f"Sprzężenie {z} = {x}")
        self._trim_memory()
        return x

    def cz_rzeczywista(self, z): # wyznaczenie części rzeczywistej liczby zespolonej
        self.memory.append(f"Część rzeczywista {z} = {z.real}")
        self._trim_memory()
        return z.real

    def cz_urojona(self,z): # wyznaczenie części urojonej liczby zespolonej
        self.memory.append(f"Część urojona {z} = {z.imag}")
        self._trim_memory()
        return z.imag

    def trygonometryczna(self, z): # przedstawienie liczby zespolonej w postaci trygonometrycznej
        modul = math.sqrt((z.real)**2 + (z.imag)**2)
        x = math.acos(z.real/modul)
        y = math.asin(z.imag/modul)
        modul1 = str(modul)
        x1 = str(x)
        y1 = str(y)
        zt = modul1 + " * (cos("+ x1 +") + isin(" + y1 + "))"
        self.memory.append(f"{z} w postaci trygonometrycznej = {zt}")
        self._trim_memory()
        return zt

    def de_moivre(self, z, n): # zastosowanie wzoru de moivre dla liczb zespolonych
        modul = abs(z)
        argument = math.atan2(z.imag, z.real)
        nowy_modul = modul ** n
        nowy_argument = argument * n
        rzeczywista = nowy_modul * math.cos(nowy_argument)
        urojona = nowy_modul * math.sin(nowy_argument)
        self.memory.append(f"{z} ^ {n} = {complex(rzeczywista,urojona)}")
        self._trim_memory()
        return complex(rzeczywista, urojona)

    def wykładnicza(self,z): # przedstawienie liczby zespolonej w postaci wykładniczej
        modul = abs(z)
        argument = math.atan2(z.imag, z.real)
        m1 = str(modul)
        arg = str(argument)
        zw = m1 + " * e^i" + arg
        self.memory.append(f"{z} w postaci wykładniczej = {zw}")
        self._trim_memory()
        return zw

    # MACIERZE

    def dodawanie_macierzy(self,a, b):  # dodawanie macierzy
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            self.memory.append(f"Macierze {a} i {b} są róznych rozmiarów")
            self._trim_memory()
            return "Nie można dodać macierzy o różnych rozmiarach."


        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[i])):
                row.append(a[i][j] + b[i][j])
            result.append(row)
        self.memory.append(f"{a} + {b} = {result}")
        self._trim_memory()
        return result

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

    def mnozenie_macierzy(self,a, b): #mnożenie macierzy
        if len(a[0]) != len(b):
            self.memory.append(f"Nie można pomnożyć macierzy {a} i {b}")
            self._trim_memory()
            return "Nie można pomnożyć tych macierzy."


        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                sum = 0
                for k in range(len(b)):
                    sum += a[i][k] * b[k][j]
                row.append(sum)
            result.append(row)
        self.memory.append(f"{a} * {b} = {result}")
        self._trim_memory()
        return result

    def odwracanie_macierzy(self,a): #wyznaczenie macierzy odwrotnej
        if len(a) != len(a[0]):
            self.memory.append(f"Macierz {a} nie ma odwrotności")
            self._trim_memory()
            return "Macierz musi być kwadratowa, aby mieć odwrotność."


        n = len(a)
        det = Kalkulator().wyznacznik_macierzy(a)
        if det == 0:
            self.memory.append(f"Macierz {a} nie ma odwrotności")
            self._trim_memory()
            return "Macierz nie ma odwrotności."


        adjugate = Kalkulator().macierz_transponowana(Kalkulator().dopelnienie_algebraiczne(a))
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(adjugate[i][j] / det)
            result.append(row)
        self.memory.append(f"Odwrotność macierzy {a} = {result}")
        self._trim_memory()
        return result

    def wyznacznik_macierzy(self, a): #liczenie wyznacznika macierzy
        if len(a) != len(a[0]):
            self.memory.append(f"Macierz {a} nie ma wyznacznika")
            self._trim_memory()
            return "Macierz musi być kwadratowa, aby obliczyć wyznacznik."


        n = len(a)
        if n == 1:
            return a[0][0]
        elif n == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        else:
            det = 0
            for j in range(n):
                det += (-1) ** j * a[0][j] * Kalkulator().wyznacznik_macierzy(Kalkulator().podmacierz(a, 0, j))
            self.memory.append(f"det{a} = {det}")
            self._trim_memory()
            return det

    def podmacierz(self,a, i, j): # podmacierz
        return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]

    def dopelnienie_algebraiczne(self,a): # dopelnienie algebraiczne
        n = len(a)
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                minor = Kalkulator().wyznacznik_macierzy(Kalkulator().podmacierz(a, i, j))
                row.append((-1) ** (i + j) * minor)
            result.append(row)
        return result

    def macierz_transponowana(self,a): # wyznaczenie macierzy transponowanej
        result = []
        for j in range(len(a[0])):
            row = []
            for i in range(len(a)):
                row.append(a[i][j])
            result.append(row)
        self.memory.append(f"Macierz transponowana macierzy {a} = {result}")
        self._trim_memory()
        return result

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

    def macierz_jednostkowa(self,n): # wyznaczenie macierzy jednostkowej
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            result.append(row)
        return result

    #POLA FIGUR

    def pole_kwadrat(self,a):
        """Oblicza pole kwadratu o boku a."""
        self.memory.append(f"Pole kwadratu o boku {a} = {a * a}")
        self._trim_memory()
        return a * a

    def pole_prostokat(self,a, b):
        """Oblicza pole prostokątao bokach a i b."""
        self.memory.append(f"Pole prostokąta o bokach {a} i {b} = {a*b}")
        self._trim_memory()
        return a * b

    def pole_trojkat(self,a, h):
        """Oblicza pole trójkąta o podstawie a i wysokości h."""
        self.memory.append(f"Pole trójkąta o podstawie {a} i wysokości {h} = {0.5 * a * h}")
        self._trim_memory()
        return 0.5 * a * h

    def pole_trapez(self,a, b, h):
        """Oblicza pole trapezu o podstawach a i b i wysokości h."""
        self.memory.append(f"Pole trapezu o podstawach {a} i {b} i wysokości {h} = {0.5 * (a + b) * h}")
        self._trim_memory()
        return 0.5 * (a + b) * h

    def pole_romb(self,a, h):
        """Oblicza pole rombu o podstawie a i wysokości h."""
        self.memory.append(f"Pole rombu o podstawie {a} i wysokości {h} = {a*h}")
        self._trim_memory()
        return a * h

    def pole_rownoleglobok(self,a, h):
        """Oblicza pole równoległoboku o podstawie a i wysokości h."""
        self.memory.append(f"Pole równoległoboku o podstawie {a} i wysokości {h} = {a*h}")
        self._trim_memory()
        return a * h

    def pole_kolo(self,r): # funkcją licząca pole koła o promieniu r
        self.memory.append(f"Pole koła o promieniu {r} = {pi * r * r}")
        self._trim_memory()
        return pi * r * r

    # FUNKCJE TRYGONOMETRYCZNE

    def sinus(self, x): # zwraca wartość funkcji sinus x
        self.memory.append(f"sin({x}) = {math.sin(x)}")
        self._trim_memory()
        return math.sin(x)

    def cosinus(self, x): # zwraca wartość funkcji cosinus x
        self.memory.append(f"cos({x}) = {math.cos(x)}")
        self._trim_memory()
        return math.cos(x)

    def tangens(self, x): # zwraca wartość funkcji tangens x
        self.memory.append(f"tg({x}) = {math.tan(x)}")
        self._trim_memory()
        return math.tan(x)

    def cotangens(self, x): # zwraca wartość funkcji cotangens x
        self.memory.append(f"ctg({x}) = {1 / math.tan(x)}")
        self._trim_memory()
        return 1 / math.tan(x)

    def arcsinus(self, x): # zwraca wartość funkcji arcus sinus x
        self.memory.append(f"arcsin({x}) = {math.asin(x)}")
        self._trim_memory()
        return math.asin(x)

    def arccosinus(self, x): # zwraca wartość funkcji arcus cosinus x
        self.memory.append(f"arccos({x}) = {math.acos(x)}")
        self._trim_memory()
        return math.acos(x)

    def arctangens(self, x): # zwraca wartość funkcji tangens x
        self.memory.append(f"arctg({x}) = {math.atan(x)}")
        self._trim_memory()
        return math.atan(x)

    def arccotangens(self, x): # zwraca wartość funkcji arcus cotangens x
        self.memory.append(f"arcctg({x}) = {math.atan(1 / x)}")
        self._trim_memory()
        return math.atan(1 / x)

    def sinh(self, x): # zwraca wartość funkcji sinus hiperboliczny x
        self.memory.append(f"sinh({x}) = {math.sinh(x)}")
        self._trim_memory()
        return math.sinh(x)

    def cosh(self, x): # zwraca wartość funkcji cosinus hiperboliczny x
        self.memory.append(f"cosh({x}) = {math.cosh(x)}")
        self._trim_memory()
        return math.cosh(x)

    def tanh(self, x): # zwraca wartość funkcji tangens hiperboliczny x
        self.memory.append(f"tgh({x}) = {math.tanh(x)}")
        self._trim_memory()
        return math.tanh(x)

    def asinh(self, x): # zwraca wartość funkcji arcus sinus hiperboliczny x
        self.memory.append(f"arcsinh({x}) = {math.asinh(x)}")
        self._trim_memory()
        return math.asinh(x)

    def acosh(self, x): # zwraca wartość funkcji arcus cosinus hiperboliczny x
        self.memory.append(f"arccosh({x}) = {math.acosh(x)}")
        self._trim_memory()
        return math.acosh(x)

    def atanh(self, x): # zwraca wartość funkcji arcus tangens hiperboliczny x
        self.memory.append(f"arctgh({x}) = {math.atanh(x)}")
        self._trim_memory()
        return math.atanh(x)

    # PIERWIASTKI ROWNANIA KWADRATOWEGO

    def pierwiastki(self, a, b, c): # obliczenie pierwiastków funkcji  z parametrów a, b, c równania
        delta = (b ** 2) - (4 * a * c)


        if delta < 0:
            self.memory.append(f"brak rzeczywistych miejsc zerowych")
            self._trim_memory()
            return "brak rzeczywistych miejsc zerowych"
        pierwiastek_delta = math.sqrt(delta)
        x1 = (-b - pierwiastek_delta) / (2 * a)
        x2 = (-b + pierwiastek_delta) / (2 * a)
        if x1 == x2:
            self.memory.append(f"x1 = {x1},")
            self._trim_memory()
            return x1


        self.memory.append(f"x1 = {x1}, x2 = {x2}")
        self._trim_memory()

        return x1, x2

    # LICZBA e

    def logarytm_naturalny(self, x): # program liczący logarytm naturalny z x
        self.memory.append(f"ln({x}) = {math.log(x)}")
        self._trim_memory()
        return math.log(x)

    def logarytm(self, x, base): # program liczący logarytm o podstawie base z x
        self.memory.append(f"log{base}({x}) = {math.log(x, base)}")
        self._trim_memory()
        return math.log(x, base)

    def potegowanie_liczby_e(self, x): # porgram liczący e do potęgi x
        self.memory.append(f"e^{x} = {math.exp(x)}")
        self._trim_memory()
        return math.exp(x)

    # POLA I OBJETOSCI BRYL OBROTOWYCH

    def pole_walca(self, promien, wysokosc): # program liczący pole walca
        pole_podstawy = math.pi * promien ** 2
        pole_boczne = 2 * math.pi * promien * wysokosc
        pole_calkowite = 2 * pole_podstawy + pole_boczne
        self.memory.append(f"Pole walca o promieniu {promien} i wysokosci {wysokosc} = {pole_calkowite}")
        self._trim_memory()
        return pole_calkowite

    def objetosc_walca(self, promien, wysokosc): # program liczący objętosc walca
        self.memory.append(f"Objętość walca o promieniu {promien} i wysokosci {wysokosc} = {math.pi * promien ** 2 * wysokosc}")
        self._trim_memory()
        return math.pi * promien ** 2 * wysokosc

    def pole_stozka(self, promien, wysokosc): # program liczący pole stożka
        pole_podstawy = math.pi * promien ** 2
        tworzaca = math.sqrt(promien ** 2 + wysokosc ** 2)
        pole_boczne = math.pi * promien * tworzaca
        pole_calkowite = pole_podstawy + pole_boczne
        self.memory.append(f"Pole stożka o promieniu {promien} i wysokosci {wysokosc} = {pole_calkowite}")
        self._trim_memory()
        return pole_calkowite

    def objetosc_stozka(self, promien, wysokosc): # program liczący objetosc stozka
        self.memory.append(
            f"Objętość stożka o promieniu {promien} i wysokosci {wysokosc} = {(1 / 3) * math.pi * promien ** 2 * wysokosc}")
        self._trim_memory()
        return (1 / 3) * math.pi * promien ** 2 * wysokosc

    def pole_kuli(self, promien): # program liczący pole kuli
        self.memory.append(f"Pole kuli o promieniu {promien}  = {4 * math.pi * promien ** 2}")
        self._trim_memory()
        return 4 * math.pi * promien ** 2

    def objetosc_kuli(self, promien): # program liczący objetosc kuli
        self.memory.append(f"Objętość kuli o promieniu {promien}  = {(4 / 3) * math.pi * promien ** 3}")
        self._trim_memory()
        return (4 / 3) * math.pi * promien ** 3

    def pole_szescianu(self, dlugosc_boku): # program liczący pole szescianu
        self.memory.append(f"Pole szescianu o dlugosci boku {dlugosc_boku}  = {6 * dlugosc_boku ** 2}")
        self._trim_memory()
        return 6 * dlugosc_boku ** 2

    def objetosc_szescianu(self, dlugosc_boku): # program liczący objetosc szescianu
        self.memory.append(f"Objętość sześcianu o dlugosci boku {dlugosc_boku}  = {dlugosc_boku ** 3}")
        self._trim_memory()
        return dlugosc_boku ** 3

    def pole_prostopadloscianu(self, dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c): # program liczący pole prostopadloscianu
        self.memory.append(f"Pole prostopadloscianu o dlugosciach boków {dlugosc_boku_a}, "
                           f"{dlugosc_boku_b}, {dlugosc_boku_c}  = "
                           f"{2 * (dlugosc_boku_a * dlugosc_boku_b + dlugosc_boku_a * dlugosc_boku_c + dlugosc_boku_b * dlugosc_boku_c)}")
        self._trim_memory()
        return 2 * (dlugosc_boku_a * dlugosc_boku_b + dlugosc_boku_a * dlugosc_boku_c + dlugosc_boku_b * dlugosc_boku_c)

    def objetosc_prostopadloscianu(self, dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c): # program liczący objetosc prostopadloscianu
        self.memory.append(f"objętość prostopadloscianu o dlugosciach boków {dlugosc_boku_a}, "
                           f"{dlugosc_boku_b}, {dlugosc_boku_c}  = "
                           f"{dlugosc_boku_a * dlugosc_boku_b * dlugosc_boku_c}")
        self._trim_memory()
        return dlugosc_boku_a * dlugosc_boku_b * dlugosc_boku_c




Calculus = Kalkulator()



Calculus.pole_stozka(1,1)


print(Calculus.memory)



Calculus.czyszczenie_pamieci()

print(Calculus.memory)