'''Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].'''

#from functools import reduce

import functools

numeri = [2, 3, 4]

result = functools.reduce (lambda a, b: a * b, numeri)

print(result)
