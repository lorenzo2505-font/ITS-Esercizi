'''Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.'''

import re


def is_integer(s: str):

    if re.fullmatch(r"^[0-9]+$", s) or re.fullmatch(r"^-[0-9]+$", s):

        return True
    
    else:

        return False
    


test = is_integer("25")

print(test)
