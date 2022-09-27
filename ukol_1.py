baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}


while True:
    kod_baliku=input("Zadej číslo balíku:")
    
    try:
        if baliky[kod_baliku]:
            print("Balík byl předán kurýrovi")
        else:
            print("Balík nebyl předán kurýrovi")
    except:
        print("Balík nenalezen")