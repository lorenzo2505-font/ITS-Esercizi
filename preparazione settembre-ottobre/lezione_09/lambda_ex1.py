from typing import Callable

'''Scrivi una funzione lambda che prenda un numero intero e ritorni il suo quadrato.'''

quadrato: Callable[[int], int] = lambda n: n**2

print(quadrato(5))