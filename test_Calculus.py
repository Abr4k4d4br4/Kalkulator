#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from Calculus import *

class MyTestCase(unittest.TestCase):
    def test_dzialania(self):
        self.assertEqual(10, Kalkulator().dodawanie(7, 3))

    def odejmowanie(self):
        self.assertEqual(-5, Kalkulator().odejmowanie(4, 9))

    def mnozenie(self):
        self.assertEqual(18, Kalkulator().mnozenie(3, 6))

    def dzielenie(self):
        self.assertEqual(2, Kalkulator().dzielenie(18, 9))
        self.assertEqual("Dzielenie przez zero!", Kalkulator().dzielenie(3, 0))

    def potegowanie(self):
        self.assertEqual(9, Kalkulator().potegowanie(3, 2))

    def pierwiastkowanie(self):
        self.assertEqual(4, Kalkulator().pierwiastkowanie(16))
        self.assertEqual("Liczba mniejsza od zera!", Kalkulator().pierwiastkowanie(-3))


    def test_calka(self):
        self.assertAlmostEqual(2, Kalkulator().calka(lambda x: x+2,-2,0,1000))


    def test_parzysta(self):
        self.assertEqual("Liczba jest liczbą parzystą", Kalkulator().parzysta(4))
        self.assertEqual("Liczba nie jest liczbą parzystą", Kalkulator().parzysta(3))


    def test_pierwsza(self):
        self.assertEqual("Liczba nie jest liczbą pierwszą", Kalkulator().czy_pierwsza(1))
        self.assertEqual("Liczba nie jest liczbą pierwszą", Kalkulator().czy_pierwsza(8))
        self.assertEqual("Liczba jest liczbą pierwszą", Kalkulator().czy_pierwsza(3))


    def test_Pochodna(self):
        self.assertAlmostEqual(6.0001, Kalkulator().pochodna(lambda x : x**2, 3))


    def test_silnia(self):
        self.assertEqual(6, Kalkulator().silnia(3))
        self.assertEqual(1, Kalkulator().silnia(0))
        self.assertEqual("liczba jest mniejsza od 0", Kalkulator().silnia(-3))

    def liczba_zespolona(self):
        self.assertEqual(3 + 4j, Kalkulator().zespolona(3, 4))

    def sprzezenie(self):
        self.assertEqual(3 - 5j, Kalkulator().sprzezenie(3 + 5j))

    def cz_rzeczywista(self):
        self.assertEqual(4, Kalkulator().cz_rzeczywista(4 - 7j))

    def czesc_urojona(self):
        self.assertEqual(-8, Kalkulator().cz_urojona(6 - 8j))

    def trygonometryczna(self):
        self.assertEqual("1.4142135623730951 * (cos(0.7853981633974484) + isin(0.7853981633974482))",
                             Kalkulator().trygonometryczna(1 + 1j))

    def test_de_Moivr(self):
        self.assertAlmostEqual((2j), Kalkulator().de_moivre((1 + 1j), 2))

    def test_wykladnicza(self):
        self.assertEqual("1.4142135623730951 * e^i0.7853981633974483", Kalkulator().wykładnicza(1+1j))

    def test_dodawanie_macierz(self):
        self.assertEqual([[6, 8], [10, 12]], Kalkulator().dodawanie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
        self.assertEqual("Nie można dodać macierzy o różnych rozmiarach.", Kalkulator().dodawanie_macierzy(
            [[1, 2], [3, 4]], [[5, 5, 9], [1, 3, 3]]))

    def test_odejmowanie_macierz(self):
        self.assertEqual([[-4, -4], [-4, -4]], Kalkulator().odejmowanie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
        self.assertEqual("Nie można odjąć macierzy o różnych rozmiarach.", Kalkulator().odejmowanie_macierzy(
                [[1, 2], [3, 4]], [[5, 5, 9], [1]]))

    def test_mnozenie_macierz(self):
        self.assertEqual([[19, 22], [43, 50]], Kalkulator().mnozenie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
        self.assertEqual("Nie można pomnożyć tych macierzy.", Kalkulator().mnozenie_macierzy([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]]))

    def test_odwracanie_macierz(self):
        self.assertEqual([[-2.0, 1.0], [1.5, -0.5]], Kalkulator().odwracanie_macierzy([[1, 2], [3, 4]]))
        self.assertEqual("Macierz musi być kwadratowa, aby mieć odwrotność.", Kalkulator().odwracanie_macierzy( [[1, 2], [3, 4], [5, 6]]))
        self.assertEqual("Macierz nie ma odwrotności.", Kalkulator().odwracanie_macierzy([[1, 1], [1, 1]]))

    def test_wyznacznik_macierzy(self):
        self.assertEqual(-2, Kalkulator().wyznacznik_macierzy([[1, 2], [3, 4]]))
        self.assertEqual("Macierz musi być kwadratowa, aby obliczyć wyznacznik.", Kalkulator().wyznacznik_macierzy([[1, 2, 3], [4, 5, 6]]))

    def test_transponowanie_macierzy(self):
        self.assertEqual([[1, 3], [2, 4]], Kalkulator().macierz_transponowana([[1, 2], [3, 4]]))

    def test_potegowanie_macierzy(self):
        self.assertEqual([[37, 54], [81, 118]], Kalkulator().potegowanie_macierzy([[1, 2], [3, 4]], 3))
        self.assertEqual("Potęga musi być liczbą nieujemną.", Kalkulator().potegowanie_macierzy([[1, 2], [3, 4]], -1))

    def test_pole_kwadrat(self):
        k = Kalkulator()
        result = k.pole_kwadrat(4)
        self.assertEqual(result, 16)

    def test_pole_prostokat(self):
        k = Kalkulator()
        result = k.pole_prostokat(3, 5)
        self.assertEqual(result, 15)

    def test_pole_trojkat(self):
        k = Kalkulator()
        result = k.pole_trojkat(6, 4)
        self.assertEqual(result, 12)

    def test_pole_trapez(self):
        k = Kalkulator()
        result = k.pole_trapez(3, 5, 4)
        self.assertEqual(result, 16)

    def test_pole_romb(self):
        k = Kalkulator()
        result = k.pole_romb(6, 4)
        self.assertEqual(result, 24)

    def test_pole_rownoleglobok(self):
        k = Kalkulator()
        result = k.pole_rownoleglobok(3, 5)
        self.assertEqual(result, 15)

    def test_pole_kolo(self):
        k = Kalkulator()
        result = k.pole_kolo(3)
        self.assertEqual(result, 28.274333882308138)


    def test_sin(self):
        self.assertEqual(Kalkulator().sinus(0), math.sin(0))
        self.assertEqual(Kalkulator().sinus(math.pi / 2), math.sin(math.pi / 2))
        self.assertEqual(Kalkulator().sinus(math.pi), math.sin(math.pi))

    def test_cos(self):
        self.assertEqual(Kalkulator().cosinus(0), math.cos(0))
        self.assertEqual(Kalkulator().cosinus(math.pi / 2), math.cos(math.pi / 2))
        self.assertEqual(Kalkulator().cosinus(math.pi), math.cos(math.pi))

    def test_tan(self):
        self.assertEqual(Kalkulator().tangens(0), math.tan(0))
        self.assertEqual(Kalkulator().tangens(math.pi / 4), math.tan(math.pi / 4))
        self.assertEqual(Kalkulator().tangens(math.pi / 2), math.tan(math.pi / 2))

    def test_cotan(self):
        self.assertEqual(Kalkulator().cotangens(math.pi / 4), 1 / math.tan(math.pi / 4))
        self.assertEqual(Kalkulator().cotangens(math.pi / 2), 1 / math.tan(math.pi / 2))

    def test_arcsin(self):
        self.assertEqual(Kalkulator().arcsinus(0), math.asin(0))
        self.assertEqual(Kalkulator().arcsinus(0.5), math.asin(0.5))
        self.assertEqual(Kalkulator().arcsinus(1), math.asin(1))

    def test_arccos(self):
        self.assertEqual(Kalkulator().arccosinus(0), math.acos(0))
        self.assertEqual(Kalkulator().arccosinus(0.5), math.acos(0.5))
        self.assertEqual(Kalkulator().arccosinus(1), math.acos(1))

    def test_arctan(self):
        self.assertEqual(Kalkulator().arctangens(0), math.atan(0))
        self.assertEqual(Kalkulator().arctangens(1), math.atan(1))
        self.assertEqual(Kalkulator().arctangens(math.inf), math.atan(math.inf))

    def test_arccotan(self):
        self.assertEqual(Kalkulator().arccotangens(1), math.atan(1 / 1))
        self.assertEqual(Kalkulator().arccotangens(0.5), math.atan(1 / 0.5))


    def test_sinh(self):
        self.assertEqual(Kalkulator().sinh(0), math.sinh(0))
        self.assertEqual(Kalkulator().sinh(1), math.sinh(1))
        self.assertEqual(Kalkulator().sinh(math.inf), math.sinh(math.inf))

    def test_cosh(self):
        self.assertEqual(Kalkulator().cosh(0), math.cosh(0))
        self.assertEqual(Kalkulator().cosh(1), math.cosh(1))
        self.assertEqual(Kalkulator().cosh(math.inf), math.cosh(math.inf))

    def test_tanh(self):
        self.assertEqual(Kalkulator().tanh(0), math.tanh(0))
        self.assertEqual(Kalkulator().tanh(1), math.tanh(1))
        self.assertEqual(Kalkulator().tanh(math.inf), math.tanh(math.inf))

    def test_asinh(self):
        self.assertEqual(Kalkulator().asinh(0), math.asinh(0))
        self.assertEqual(Kalkulator().asinh(1), math.asinh(1))
        self.assertEqual(Kalkulator().asinh(math.inf), math.asinh(math.inf))

    def test_acosh(self):
        self.assertEqual(Kalkulator().acosh(1), math.acosh(1))
        self.assertEqual(Kalkulator().acosh(2), math.acosh(2))
        self.assertEqual(Kalkulator().acosh(math.inf), math.acosh(math.inf))

    def test_atanh(self):
        self.assertEqual(Kalkulator().atanh(0.5), math.atanh(0.5))


    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_oblicz_pierwiastki(self):
        # Przykładowe dane
        a = 1
        b = -5
        c = 6

        # Oczekiwane wyniki
        expected_x1 = 2
        expected_x2 = 3

        # Obliczanie pierwiastków
        x1, x2 = self.kalkulator.pierwiastki(a, b, c)

        # Porównanie wyników z oczekiwanymi
        self.assertAlmostEqual(x1, expected_x1)
        self.assertAlmostEqual(x2, expected_x2)

    def test_oblicz_logarytm_naturalny(self):
        result = self.kalkulator.logarytm_naturalny(10)
        self.assertAlmostEqual(result, math.log(10))

    def test_oblicz_logarytm(self):
        result = self.kalkulator.logarytm(8, 2)
        self.assertAlmostEqual(result, math.log(8, 2))

    def test_oblicz_potegowanie_liczby_e(self):
        result = self.kalkulator.potegowanie_liczby_e(2)
        self.assertAlmostEqual(result, math.exp(2))

    def test_oblicz_pole_walca(self):
        promien = 3
        wysokosc = 5
        pole_walca = self.kalkulator.pole_walca(promien, wysokosc)
        self.assertEqual(pole_walca, 150.79644737231007)

    def test_oblicz_objetosc_walca(self):
        promien = 3
        wysokosc = 5
        objetosc_walca = self.kalkulator.objetosc_walca(promien, wysokosc)
        self.assertEqual(objetosc_walca, 141.3716694115407)

    def test_oblicz_pole_stozka(self):
        promien = 4
        wysokosc = 6
        pole_stozka = self.kalkulator.pole_stozka(promien, wysokosc)
        self.assertEqual(pole_stozka, 140.8828696505485)

    def test_oblicz_objetosc_stozka(self):
        promien = 4
        wysokosc = 6
        objetosc_stozka = self.kalkulator.objetosc_stozka(promien, wysokosc)
        self.assertEqual(objetosc_stozka, 100.53096491487338)

    def test_oblicz_pole_kuli(self):
        promien = 5
        pole_kuli = self.kalkulator.pole_kuli(promien)
        self.assertEqual(pole_kuli, 314.1592653589793)

    def test_oblicz_objetosc_kuli(self):
        promien = 5
        objetosc_kuli = self.kalkulator.objetosc_kuli(promien)
        self.assertEqual(objetosc_kuli, 523.5987755982989)

    def test_oblicz_pole_szescianu(self):
        dlugosc_boku = 4
        pole_szescianu = self.kalkulator.pole_szescianu(dlugosc_boku)
        self.assertEqual(pole_szescianu, 96)

    def test_oblicz_objetosc_szescianu(self):
        dlugosc_boku = 4
        objetosc_szescianu = self.kalkulator.objetosc_szescianu(dlugosc_boku)
        self.assertEqual(objetosc_szescianu, 64)

    def test_oblicz_pole_prostopadloscianu(self):
        dlugosc_boku_a = 3
        dlugosc_boku_b = 4
        dlugosc_boku_c = 5
        pole_prostopadloscianu = self.kalkulator.pole_prostopadloscianu(dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c)
        self.assertEqual(pole_prostopadloscianu, 94)

    def test_oblicz_objetosc_prostopadloscianu(self):
        dlugosc_boku_a = 3
        dlugosc_boku_b = 4
        dlugosc_boku_c = 5
        objetosc_prostopadloscianu = self.kalkulator.objetosc_prostopadloscianu(dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c)
        self.assertEqual(objetosc_prostopadloscianu, 60)




if __name__ == '__main__':
    unittest.main()
