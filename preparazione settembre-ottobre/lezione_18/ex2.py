'''Validazione della password 1: scrivere una funzione validate_password(password) che verifichi se una password soddisfa i seguenti criteri:
lunghezza minima di 20 caratteri, almeno tre lettere maiuscole, 
almeno quattro caratteri speciali (non alfanumerici). 
Se la password è valida, la funzione deve restituire True. 
Se la password non è valida, 
la funzione deve generare un'eccezione predefinita (ad esempio, ValueError) 
con un messaggio che indica quali criteri non sono stati soddisfatti.'''

from string import ascii_uppercase
from string import punctuation


def validate_password(password: str) -> bool:

    u = ascii_uppercase
    cont_u = 0

    p = punctuation
    cont_p = 0
    
    if len(password) < 20:

        raise ValueError("la password deve essere lunga di almeno 20 caratteri")
    
    for i in password:

        if i in u:
            cont_u += 1
        
        elif i in p:
            cont_p += 1
    
    if cont_u < 3:
        
        raise ValueError("la password deve avere almeno 3 lettere maiuscole")
    
    if cont_p < 4:

        raise ValueError("la password deve avere almeno 4 caratteri speciali")
    
    return True

print(validate_password("aaaaaaa"))
    
    
    
    