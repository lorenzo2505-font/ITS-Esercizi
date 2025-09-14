'''Validazione password 2:
scrivere una funzione validate_password(password) 
che verifichi se una password soddisfa determinati criteri
(ad esempio, lunghezza minima di 20 caratteri, 
almeno tre caratteri maiuscoli e almeno quattro caratteri speciali). 
Generare un'eccezione personalizzata (ad esempio, InvalidPasswordError) per le password non valide.'''

from custom_ex import InvalidPasswordError


from string import ascii_uppercase
from string import punctuation


def validate_password2(password: str) -> bool:

    u = ascii_uppercase
    cont_u = 0

    p = punctuation
    cont_p = 0
    
    if len(password) < 20:

        raise InvalidPasswordError()
    
    for i in password:

        if i in u:
            cont_u += 1
        
        elif i in p:
            cont_p += 1
    
    if cont_u < 3:
        
        raise InvalidPasswordError()
    
    if cont_p < 4:

        raise InvalidPasswordError()
    
    return True

print(validate_password2("aaaaaaa"))