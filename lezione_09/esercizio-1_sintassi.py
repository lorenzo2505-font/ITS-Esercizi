'''Scrivi una funzione lambda che prenda un numero intero e ritorni il suo quadrato.

Esempio atteso:

quadrato = lambda x: ...'''

from typing import Callable

power: Callable [[int], int] = lambda a: a**2

print(power(int(input("inserisci numero: "))))

''''''