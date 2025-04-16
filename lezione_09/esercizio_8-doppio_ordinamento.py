'''Hai una lista di dizionari:

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

Ordina la lista in ordine decrescente di media usando una funzione lambda.'''

from typing import Callable

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

order_stud: list = sorted(studenti, key = lambda i: i["media"])

print(order_stud)




