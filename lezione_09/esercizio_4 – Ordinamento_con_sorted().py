'''Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]. 
Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.'''

from typing import Callable 

studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

sorted_age: list  = sorted(studenti, key = lambda age: age[1] )

print(sorted_age)

