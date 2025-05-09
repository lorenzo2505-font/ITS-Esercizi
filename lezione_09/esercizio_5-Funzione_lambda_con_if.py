'''Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".'''

from typing import Callable 

numero: Callable [[int], str] = lambda esito: "pari" if esito % 2 == 0 else "dispari"