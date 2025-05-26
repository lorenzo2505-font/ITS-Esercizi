'''Crea una funzione che generi una password casuale con una lunghezza specifica e i tipi di caratteri desiderati

(lettere minuscole, lettere maiuscole, numeri, simboli).

Consenti all'utente di specificare la lunghezza della password e i tipi di caratteri desiderati.

Genera e restituisci una password casuale che soddisfi i criteri dell'utente.'''

import random


def casual_password (lunghezza: int, caratteri: list) -> str:

    psw: str = ""

    cont = 0

    password: list[str] = []

   

    for i in range(len(caratteri)):

        if caratteri[i] is not str:

            caratteri[i] = str(caratteri[i])
            
        else:
            pass
        
        
    for i in range(lunghezza):

        c = random.choice(caratteri)

        psw += c
    
    return psw




        
    


t = casual_password(4, ["L", "i", True, 5, 6])

print(t)









    

    

