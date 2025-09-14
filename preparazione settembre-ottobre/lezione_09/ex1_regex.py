'''Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti'''
import re

def is_integer(s: str) -> bool:

    if re.fullmatch(r"^[0-9]+$", s) or re.fullmatch(r"^-[0-9]+$", s):

        return True
    
    return False


print(is_integer("123"))
print(is_integer("-456"))
print(is_integer("12.3"))