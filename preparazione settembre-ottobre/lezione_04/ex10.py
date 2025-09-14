'''Crea una funzione che verifichi se due stringhe date sono anagrammi l'una dell'altra.

Converti entrambe le stringhe in minuscolo e rimuovi tutti i caratteri non alfabetici.

Ordina i caratteri di ciascuna stringa e confronta le stringhe ordinate per verificarne l'uguaglianza.

Indica se le stringhe sono anagrammi o meno.'''

from string import ascii_lowercase


def anagramma(s1: str, s2: str):

    s1_list: list = []
    s2_list: list = []

    alphabet = ascii_lowercase
    
    
    for i in s1:

        if i.isupper():
            s1_list.append(i.lower())
        
        elif i not in alphabet:
            continue
        
        else:
            s1_list.append(i)
    
    for i in s2:

        if i.isupper():
            s2_list.append(i.lower())
        
        elif i not in alphabet:
            continue
        
        else:
            s2_list.append(i)
    
    if sorted(s1_list) == sorted(s2_list):

        return True
    
    return False

print(anagramma("Cine", "Nice"))



    

    
    


        
