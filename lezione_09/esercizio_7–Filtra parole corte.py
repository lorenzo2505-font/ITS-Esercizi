'''Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"]
 Estrai solo le parole con più di 4 lettere usando filter() e lambda.'''

from typing import Callable

parole: list [str] = ["cane", "gatto", "elefante", "ratto", "orso"]

quattro_lettere: list[str] = list(filter(lambda x: len(x) == 4, parole))

print(quattro_lettere)