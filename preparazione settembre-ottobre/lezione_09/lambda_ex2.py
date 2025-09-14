'''Esercizio 2 - Somma di due numeri
Crea una funzione lambda che accetti due numeri e restituisca la loro somma.'''

from typing import Callable

somma: Callable[[int, int], int] = lambda a, b: a + b

print(somma(1, 3))