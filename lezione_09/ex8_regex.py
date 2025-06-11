'''Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e/o numeri.

Esempio:

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678', 'XYZZYZZZ']'''

import re


def find_codes(text: str) -> list:


    codes = re.findall(r"[A-Z0-9]{8}", text)

    return codes


test = find_codes("I codici sono AB12CD34 e 12345678 e XYZZYZZZ")

print(test)

