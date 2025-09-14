'''Scrivere una regex per verificare se una stringa contiene solo lettere maiuscole.'''
import re


mystr: str = "POPA"

if re.fullmatch(r"^[A-Z]+$", mystr):
    
    print(mystr)

else:
    
    print(False)

