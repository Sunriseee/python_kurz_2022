
# 1 https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/funkce/excs
from calendar import month
from types import MethodDescriptorType


def mult(a, b):
    return a * b


print(mult(1, 3))

# 2


def total_price(persons, breakfast=False):
    night_price = 850
    breakfast_price = 125

    nights_total = night_price * persons
    breakfast_total = 0
    if breakfast:
        breakfast_total += breakfast_price * persons
    return nights_total + breakfast_total


print(total_price(10, False))
# 3


def month_of_birth(rodne_cislo):
    pass
