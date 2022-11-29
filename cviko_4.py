from json import JSONEncoder


class Jednorozec:
    def vypis_informace(self):
        print(f'Jmenuju se {self.jmeno}' a mam {self.barva} barvu')


karel = Jednorozec()
karel.jmeno = 'Karel'
karel.barva = 'duhovou'

lenmka = Jednorozec
lenka.jmeno = 'Lenka'
lenka.barva = 'pruhovanou'

navratova_hodnota = karel.vypis_informace()
