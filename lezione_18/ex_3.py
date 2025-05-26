'''Scrivi una funzione validate_password(password) che verifichi se una password soddisfa determinati criteri
(ad esempio, lunghezza minima di 20 caratteri, almeno tre caratteri maiuscoli e almeno quattro caratteri speciali).
Genera un'eccezione personalizzata (ad esempio, InvalidPasswordError) per le password non valide.'''

import string

from eccezioni_personalizzate import InvalidPasswordError


def validate_password(password: str):

    conta_maiuscole = 0

    conta_speciali = 0

    speciali = string.punctuation #includes common special characters

    for i in password:

        if i == i.upper():

            conta_maiuscole += 1
        
        if i in speciali:

            conta_speciali += 1
        

        

    if (len(password) >= 20) and (conta_maiuscole >= 3) and (conta_speciali >= 4):

        return True
    
    else:

        raise InvalidPasswordError (f"la password deve avere almeno 20 caratteri, 3 maiuscole, 4 caratteri speciali, caratteri: {len(password)}, maiuscole: {conta_maiuscole}, speciali: {conta_speciali}")
    


t = validate_password ("bozzo")


print(t)




