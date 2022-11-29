class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti


class Koronavirus (Nemoc):
    def __init__(self, jmeno, pocet_obeti, sireni, inkubacni_doba):
        super().__init__(jmeno, pocet_obeti, sireni, inkubacni_doba)
        super().zmen_pocet_obeti(self.pocet_obeti)
        self.varianty = []

    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)

    def __str__(self):
        self.jmeno
        self.varianty


corona = Koronavirus('Coronavirus', 5, 100, 'vzduchem')
print(corona)
corona.pridej_variantu('omikron')
print(corona)
