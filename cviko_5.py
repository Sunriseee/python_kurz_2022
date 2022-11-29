# dědičnost - vysvětleno na manažerovi
class Zamestnanec:
    def __init__(self, jmeno: str, pozice: str):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self):
        return f'{self.jmeno} pracuje na pozici {self.pozice}'

    def cerpani_dovolene(self, pocet_dni):
        if pocet_dni <= self.pocet_dni_dovolene:
            self.pocet_dni_dovolene -= pocet_dni
            return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
        else:
            return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'


frantisek = Zamestnanec('Frantisek', 'Programator')
print(frantisek.cerpani_dovolene(5))
print(frantisek.cerpani_dovolene(15))
print(frantisek.cerpani_dovolene(10))


# class Manazer:
#   def __init__(self, jmeno: str, pozice: str):
#   self.jmeno = jmeno
#    self.pozice = pozice
#   self.pocet_dni_dovolene = 30
#   self.pocet_podrizenych = 10

# def __str__(self):
#     return f'{self.jmeno} pracuje na pozici {self.pozice}'

# def cerpani_dovolene(self, pocet_dni):
#  if pocet_dni <= self.pocet_dni_dovolene:
#       self.pocet_dni_dovolene -= pocet_dni
#      return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
#  else:
#      return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'


class Manazer(Zamestnanec):  # závorka určuje z jaké třídy se dědí, dá se dědit z více tříd, ale moc to většinou v pythonu nedává smysl
    def __init__(self, jmeno, pocet_podrizenych):
        # super uvrací objekt nadřezené třídy a tím může volat cokoliv, co ta třída má
        super().__init__(jmeno, 'Manazer')
    # zároveň můžu pak v této třídě přepisovat a dopisovat
        self.pocet_dni_dovolene = 30
        self.pocet_podrizenych = pocet_podrizenych

    def __str__(self):
        return f'{super().__str__()} a má {self.pocet_podrizenych} podřízených'


martin = Manazer('Martin', 10)
print(martin)
