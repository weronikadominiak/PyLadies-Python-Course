# Stwórz - z wykorzystaniem klas i dziedziczenia - kalkulator objętości brył:
# sześcianu, prostopadłościanu, stożka i kuli.
# Powinien on wczytać od użytkownika opcję (0, 1, 2 lub 3) i w zależności od tego przyjąć
# 3 argumenty, 2 lub 1 i obliczyć objętość. Na wszelki wypadek wzory na objętość podane poniżej.
# Sześcian: V = a^3
# Prostopadłościan: V = a*b*c
# Kula: V = 4/3 * pi * r^3


class Bryla:

    def __init__(self, wzor):
        self.wzor = wzor

    def zapytaj_uzytkownika(self):
        odp = input("Wybierz opcje 0, 1, 2, 3: \n")
        return odp


class Szescian(Bryla):
    def __init__(self):
        pass

    def pobierz_dane(self):
        a = input("Podaj wartosc a: \n")


class Prostopadloscian(Bryla):
    def __init__(self):
        pass

    def pobierz_dane(self):
        a = input("Podaj wartosc a: \n")
        b = input("Podaj wartosc b: \n")
        c = input("Podaj wartosc c: \n")


class Kula(Bryla):
    def __init__(self):
        pass

    def pobierz_dane(self):
        r = input("Podaj wartosc r: \n")

x = Bryla.zapytaj_uzytkownika(Bryla)
x = int(x)
if x == 1:
    Szescian.pobierz_dane(Szescian)
elif x == 2:
    Prostopadloscian.pobierz_dane(Prostopadloscian)
elif x == 3:
    Kula.pobierz_dane(Kula)
else:
    print("Papa")