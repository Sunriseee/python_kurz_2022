
from datetime import datetime, timedelta

cas_vstupu = input("Zadej čas vstupu:")
pocet_osob = input("Zadej počet osob: ")

print(datetime.strptime(cas_vstupu, "%d. %m. %Y"))
print(pocet_osob)


otevreno_od1 = datetime.strptime("1. 7. 2022", "%d. %m. %Y")
otevreno_do1 = datetime.strptime("10. 8. 2022", "%d. %m. %Y")

otevreno_od2 = datetime.strptime("11. 8. 2022", "%d. %m. %Y")
otevreno_do2 = datetime.strptime("31. 8. 2022", "%d. %m. %Y")


#print(otevreno_od1, "%d. %m. %Y")

cena = 0


def spoctiCenu():
    cena * pocet_osob


def oteviraciDoba():

    if cas_vstupu >= otevreno_od1 and cas_vstupu <= otevreno_do1:
        cena = 250
        print(cena)
        print(spoctiCenu())
    elif cas_vstupu >= otevreno_od2 and cas_vstupu <= otevreno_do2:
        cena = 180
        vstupne = cena * pocet_osob
        print(spoctiCenu())
    else:
        print("Je zavřeno!")


print(cena)
print(pocet_osob)
