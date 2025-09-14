'''Scrivi una funzione is_valid_cap(cap) che restituisce True se il CAP è valido (5 cifre), False altrimenti.'''
import re

def is_valid_cap(cap: str):

    if re.fullmatch(r"[0-9]{5}", cap):

        return True
    
    return False

print(is_valid_cap("70124"))
print(is_valid_cap("A0123"))