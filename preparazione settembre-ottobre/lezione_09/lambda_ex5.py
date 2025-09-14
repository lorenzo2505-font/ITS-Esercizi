'''Esercizio 5 - Funzione lambda con if
Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".'''

from typing import Callable

pari_dispari: Callable[[int], str] = lambda n : "pari" if n % 2 == 0 else "dispari"

print(pari_dispari(1))
print(pari_dispari(2))