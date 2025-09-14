'''Scrivere una regex per trovare tutte le occorrenze di "cat" in una stringa.'''
import re

mystr: str = "cat pat lab cat"


occ_cat: list[str] = re.findall(r"cat", mystr)

print(occ_cat)