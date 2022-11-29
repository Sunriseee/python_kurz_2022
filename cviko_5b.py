# chci navýši známky o 1

pisemky = [0, 2, 0, 1, 1, 3]
pisemky_1 = []
for znamka in pisemky:
    pisemky_1.append(znamka+1)
print(pisemky_1)

# další možnost je zápis jako list comprehension
print([znamka + 1 for znamka in pisemky])

# pomocí tohoto můžu ale i vnořovat o sebe pomocí dalšího for - specifika pythonu - aneb jak napsat spoustu věcí na jeden řádek

# teď chcí zvýšit o 1 tam kde je 0
pisemky_1 = []
for znamka in pisemky:
    nova_znamka = znamka
    if znamka == 0:
        nova_znamka += 1
    pisemky_1.append(znamka+1)
print(pisemky_1)

# přepis do list compr. se nám zamotal, ale obecně se to často používá a filtraci
