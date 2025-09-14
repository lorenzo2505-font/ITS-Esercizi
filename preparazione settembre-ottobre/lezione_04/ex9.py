'''Crea funzioni per crittografare e decrittografare un messaggio utilizzando il cifrario di Cesare.

Consenti all'utente di specificare il valore di shift (numero di posizioni di cui spostare ogni lettera).

Gestisci sia la crittografia che la decrittografia utilizzando la stessa funzione con le opportune modifiche.

Crittografa e decrittografa il messaggio specificato utilizzando il valore di shift specificato.'''

from string import ascii_lowercase
from string import ascii_uppercase


def encripta(parola: str, shift: int):
    l = ascii_lowercase
    u = ascii_uppercase
    parola_encriptata: str = ""

    while shift > 26:
        shift -= 26
    
    for i in range(len(parola)):
        
        if parola[i] in l:

            for j in range(len(l)):

                if l[j] == parola[i]:
                    

                    parola_encriptata += l[(j + shift) % len(l)] # l'operatore modulo da il resto della divisione evitando l'index error
                    
        elif parola[i] in u:

            for j in range(len(u)):

                if u[j] == parola[i]:
                    parola_encriptata += u[(j + shift) % len(u)] # l'operatore modulo da il resto della divisione evitando l'index error
        
        else:
            parola_encriptata += parola[i]
    
    return parola_encriptata



print(encripta("z", 3))




        
    
    
    



    



