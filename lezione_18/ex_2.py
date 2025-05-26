'''Scrivi una funzione validate_password(password) che verifichi se una password soddisfa i seguenti criteri: 
lunghezza minima di 20 caratteri, almeno tre lettere maiuscole, almeno quattro caratteri speciali (non alfanumerici). 
Se la password è valida, la funzione deve restituire True. Se la password non è valida, la funzione deve generare un'eccezione predefinita 
(ad esempio, ValueError) con un messaggio che indica quali criteri non sono stati soddisfatti.'''

import string


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

        raise Exception(f"la password deve avere almeno 20 caratteri, 3 maiuscole, 4 caratteri speciali, caratteri: {len(password)}, maiuscole: {conta_maiuscole}, speciali: {conta_speciali}")
    
  
 
    



t = validate_password("aaaaaaaaaA$")

print(t)








    



