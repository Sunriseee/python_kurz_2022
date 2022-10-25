from ast import AugStore
from pickle import TRUE


class Recept:
    def __init__(self, nazev: str, narocnost: int, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        return f'Návod na {self.nazev} je zde: {self.url_adresa}. Jedná se o recept náročný na {self.narocnost} z 5.'

    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota
        return f'náročnost: {self.narocnost}'

    def zkusit(self):
        self.vyzkouseno = True
        if self.vyzkouseno == True:
            return f'vyzkoušeno'
        else:
            return f'nevyzkoušeno'


tiramisu = Recept('tiramisu', 5, 'www.recepty.cz/tiramisu')
pernik = Recept('pernik', 11, 'www.recepty.cz/pernik')
print(tiramisu)

print(tiramisu.zkusit())
print(tiramisu.zmen_narocnost(1))
print(tiramisu)


class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return f'{self.nazev} od {self.autor}'

    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)

    def pocet_receptu(self):
        pocet_receptu = len(self.recepty)
        return f'V kuchařce je {pocet_receptu} receptů.'


moje_kucharka = Kucharka('Dezerty', 'maminka')
moje_kucharka.pridej_recept(pernik)
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pocet_receptu()
print(moje_kucharka)
print(moje_kucharka.pocet_receptu())
