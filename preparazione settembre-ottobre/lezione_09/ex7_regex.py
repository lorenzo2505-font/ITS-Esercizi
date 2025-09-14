'''Scrivi una funzione is_valid_name(name) che controlla se la stringa inizia con una lettera maiuscola seguita da almeno due lettere minuscole.'''
import re

def is_valid_name(name: str) -> bool:

    if re.fullmatch(r"^[A-Z]{1}[a-z]{2,}", name):

        return True
    
    return False

print(is_valid_name("Marco"))
print(is_valid_name("marco"))
print(is_valid_name("Ma"))