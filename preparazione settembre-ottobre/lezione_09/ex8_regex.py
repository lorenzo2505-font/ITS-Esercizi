'''Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e/o numeri.'''
import re

def find_codes(text: str):

    occ: list = re.findall(r"[A-Z0-9]{8}", text)

    return occ

print(find_codes("I codici sono AB12CD34 e 12345678 e XYZZYZZZ"))

