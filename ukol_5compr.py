
# https: // kodim.cz/kurzy/python-data/zaklady-programovani/text-chroustani/chroustani-seznamu - ukol 1

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
nasobky = [hodnota*2 for hodnota in cisla]
print(nasobky)

zmena_znamenka = [hodnota*-1 for hodnota in cisla]
print(zmena_znamenka)

mocnina = [hodnota ** 2 for hodnota in cisla]
print(mocnina)

retezec = [str(hodnota) for hodnota in cisla]
print(retezec)

# https: // kodim.cz/kurzy/python-data/zaklady-programovani/text-chroustani/chroustani-seznamu - ukol 2
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
pocty_pismen = [len(kluk) for kluk in jmena]
print(pocty_pismen)

velka_pismena = [kluk.upper() for kluk in jmena]
print(velka_pismena)

holka = [kluk+"a" for kluk in jmena]
print(holka)

emaily = [kluk.lower()+"@email.cz" for kluk in jmena]
print(emaily)
