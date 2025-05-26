'''Radice quadrata sicura: scrivi una funzione safe_sqrt(numero) che calcoli la radice quadrata di un numero utilizzando math.sqrt(). 
Gestisci ValueError se l'input è negativo restituendo un messaggio informativo.'''

import math


def safe_sqrt(n: int):

    rad_n = math.sqrt(n)

    print(rad_n)


try:

    safe_sqrt(-1)

except ValueError:

    print("il numero che hai inserito è negativo")

