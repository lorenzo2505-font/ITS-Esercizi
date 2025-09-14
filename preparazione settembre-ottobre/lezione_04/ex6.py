import random
from string import ascii_letters
from string import punctuation
from string import ascii_lowercase
from string import ascii_uppercase


'''6. Generatore di password:

Crea una funzione che genera una password casuale con una lunghezza specificata e i tipi di caratteri desiderati
(lettere minuscole, lettere maiuscole, numeri, simboli).

Consenti all'utente di specificare la lunghezza della password e i tipi di caratteri desiderati.

Genera e restituisce una password casuale che soddisfi i criteri dell'utente.'''


def generaPassword(lunghezza: int, minuscoli: bool = False, maiuscoli: bool = False, numeri: bool = False, speciali: bool = False):

    password: str = ""

    characters: list = []

    if minuscoli:
        characters += ascii_lowercase
    
    if maiuscoli:
        characters += ascii_uppercase
    
    if numeri:
        characters += [x for x in range(9 + 1)]
    
    if speciali:
        characters += punctuation
    
    for i in range(lunghezza):
        password += str(random.choice(characters))
    
    if not(password):
        
        return None
    
    return password


print(generaPassword(8, minuscoli = True, numeri = True))

    

    
    


    




