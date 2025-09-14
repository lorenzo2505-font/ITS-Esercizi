'''Esercizio 6 - Uso con reduce()
Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].'''

import functools

numeri: list[int] = [2, 3, 4]

prodotti = functools.reduce(lambda a, b: a * b, numeri) 

print(prodotti)