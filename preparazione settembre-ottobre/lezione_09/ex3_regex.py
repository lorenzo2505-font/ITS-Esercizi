'''Scrivi una funzione mask_numbers(text) che sostituisce tutte le sequenze di cifre con ###.'''
import re

def mask_numbers(text: str) -> str:

    sub = re.sub(r"[0-9]", "#", text)

    return sub

print(mask_numbers("Il codice è 12345 e la data è 2025."))