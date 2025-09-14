'''Radice quadrata sicura: scrivi una funzione safe_sqrt(number) che calcoli la radice quadrata di un numero utilizzando math.sqrt().
Gestisci ValueError se l'input è negativo restituendo un messaggio informativo.'''

import math

def safe_sqrt(number: int):
    
    if number < 0:

        raise ValueError("non si può fare la radice quadrata di un numero negativo")
    
    return math.sqrt(number)

print(safe_sqrt(25))