
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}


for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)

soucet = 0
for znamka in school_report.values():
    soucet += znamka  # příčítá známky
    prumer = soucet/len(school_report)
print(prumer)

for key, value in school_report.items():
    # potřebujeme se dostat jak do klíče, tak do hodnoty, proto item
    if value == 1:
        print(key)


books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
pocet_stran = 0
for item in books:
    pocet_stran += item["pages"]
print(pocet_stran)


for item in books:
    if item["rating"] >= 8:
        print(item["title"])

# onus je řešením if key[1]=="P":
