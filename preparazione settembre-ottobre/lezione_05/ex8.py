'''Generare una lista di numeri interi casuali e utilizzare una list comprehension per selezionare solo quelli che sono multipli di 3.'''

import random

casual_numbers: list[int] = [random.randint(1, 100) for x in range(10)]

mylist: list[int] = [i for i in casual_numbers if i % 3 == 0]

print(mylist)