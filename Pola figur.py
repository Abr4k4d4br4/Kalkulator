class Kalkulator:

    def pole_kwadrat(a):
        """Oblicza pole kwadratu."""
        return a * a


    def pole_prostokat(a, b):
        """Oblicza pole prostokąta."""
        return a * b


    def pole_trojkat(a, h):
        """Oblicza pole trójkąta."""
        return 0.5 * a * h


    def pole_trapez(a, b, h):
        """Oblicza pole trapezu."""
        return 0.5 * (a + b) * h


    def pole_romb(a, h):
        """Oblicza pole rombu."""
        return a * h


    def pole_rownoleglobok(a, h):
        """Oblicza pole równoległoboku."""
        return a * h

    def pole_kola(r):
        """Oblicza pole koła."""
        return r * r * 3.14

    def pole_szesciokat(a):
        """Oblicza pole sześćiokąta foremnego."""
        return a * a * (3**1/2) * 3 / 2


    def pole_trojakt_rownoboczny(a, h):
        """Oblicza pole trójkąta równobocznego"""
        return a * a * (3**1/2) / 4

    def pole_trojakt_prostokątny(a, b):
        """Oblicza pole trójkąta prostokątnego"""
        return a * b /2


    def pole_trojakt_kat(a, b, s):
        """Oblicza pole trójkąta znajac boki oraz sinus kąta pomiędzy nimi"""
        return a * b * s /2

    def pole_romb(d1, d2):
        """Oblicza pole rombu znając długości przekątnych."""
        return d1 * d2 /2