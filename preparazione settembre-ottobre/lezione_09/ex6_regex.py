'''Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.'''
import re

def check_product_code(code: str):

    if re.fullmatch(r"^[A-Z]{4}-[0-9]{4}-[A-Z]{2}$", code):

        return True
    
    return False

print(check_product_code("PROD-9876-ZX"))
print(check_product_code("PROD-99-ZX"))