import csv
with open('python_kurz_2022/Znamky.csv', 'r', encoding='utf-8', newline='') as znamky:
    radky = csv.reader(znamky, delimiter=' ', quotechar='|')
 #    nadpis = next(znamky)
    # radky_bez_nadpisu = next(radky)
    nove_znamky_vystup = " "
    cislo_radku = 1

    for radek in radky:
        nova_znamka = (' '.join(radek))

        if cislo_radku > 1:
            nova_znamka = nova_znamka.replace("1", "A")
            nova_znamka = nova_znamka.replace("2", "B")
            nova_znamka = nova_znamka.replace("3", "C")
            nova_znamka = nova_znamka.replace("4", "D")
            nova_znamka = nova_znamka.replace("5", "F")
            print(nova_znamka)

        cislo_radku = cislo_radku + 1
        nove_znamky_vystup = nove_znamky_vystup + nova_znamka + '\n'

    with open('python_kurz_2022/Znamky_nove.csv', mode='w', encoding='utf-8') as vystup:
        vystup.writelines(nove_znamky_vystup)
