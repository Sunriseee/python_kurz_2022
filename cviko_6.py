
# https: // kodim.cz/kurzy/python-data/zaklady-programovani/soubory/zapis-souboru
with open('python_kurz_2022/mereni.txt', 'r', encoding='utf-8') as file:
    radky = file.readlines()

# print(radky)

# radky_bez_newline = []
# for radek in radky:
#     radky_bez_newline.append(radek.replace('\n', ''))

# radky_bez_newline = [radek.rstrip() for radek in radky]
jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
jmena_radky = [jmeno + '\n' for jmeno in jmena]

with open('uzivatele.txt', mode='w', encoding='utf-8') as vystup:

    # jmena_radky = []
    # for jmeno in jmena:
    #     jmena_radky.append(jmeno + '\n')

    vystup.writelines(jmena_radky)

jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as file:

    for jmeno in jmena:
        file.write(jmeno + ' :-)\n')
