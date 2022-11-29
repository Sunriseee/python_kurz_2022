def greet_user(name):
    print(f'Ahoj {name}')


greet_user('Veronika')


def greet_user(name: str, age: int):
    print(f'Ahoj {name} {age}')


greet_user('Veronika', 2)


pocet = len("abcd")
print(pocet)


# defaultně 0, ale když ho specifikuju níže, změním jej, když tam default nedám, musí být definovaný
def vypocti_znamku(body, bonusove_body=0):
    celkove_body = body + bonusove_body
    if celkove_body > 20:
        return 1
    return 5


body = int(input('Zadej body: '))
print(vypocti_znamku(body))


def total_price(persons, breakfast=False):
    night_price = 850
    breakfast_price = 125

    nights_total = night_price * persons
    breakfast_total = 0
    if breakfast:
        breakfast_total += breakfast_price * persons
    return nights_total + breakfast_total


print(total_price(10, False))
