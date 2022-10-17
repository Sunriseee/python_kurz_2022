
from operator import truediv
from pickle import TRUE

telefon = input(str("Zadej telefonní číslo: "))
cena_znaku = int(3)


def overCislo(telefon):
    telefonCheck = telefon.replace(" ", "")

    if len(telefonCheck) == 9:
        return True
    elif len(telefonCheck) == 13 and telefonCheck[0:4] == str("+420"):
        return True
    else:
        return False


def spoctiCenu(zprava):
    cena = round(len(zprava)/180)*cena_znaku
    if cena < 1:
        return 1*cena_znaku
    else:
        return cena


# if že to je či není číslo a výsledek dle toho
kontrola = overCislo(telefon)
if kontrola == True:
    print("Cislo je validni")
    zprava = input(str("Zadej text SMS: "))
    cena = spoctiCenu(zprava)
    print(f"Cena SMS zprávy je:{cena} Kč")


else:
    print("Cislo neni validni!!")
