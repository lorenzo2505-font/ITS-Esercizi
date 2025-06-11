'''Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

Esempio:

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False'''


import re





def check_product_code(code: str) -> bool:


    if re.fullmatch(r"^[A-Z]{4}-[0-9]{4}-[A-Z]{2}", code):

        return True
    
    else:

        return False
    


test = check_product_code("PROD-9876-ZX")

print(test)


