from turtle import title


sales = {
    "A": 4165,
    "B": 5681,
    "C": 2652,
}

for book in sales.items():
    print(book)

# tuple list, ale nelze už vypsanou hodnotu upravit
# list vypíše klíč i hodnotu

# vícerozměrné slovníky
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]


for book in books:
    print(book['year'])


for item in [1, 2, 3, 4]:
    print(item)

for item in "Hana":
    print(item)

slovnik = {1: "a", 2: "b"}
