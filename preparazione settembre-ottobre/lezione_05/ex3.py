'''Scrivere una list comprehension che estrae solo i numeri pari da una lista.'''


numeri: list[int] = [x for x in range(9)]

numeri_pari: list[int] = [i for i in numeri if i % 2 == 0]

print(numeri_pari)