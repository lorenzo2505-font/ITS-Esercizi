'''Radice quadrata sicura: scrivi una funzione safe_sqrt(numero) che calcoli la radice quadrata di un numero utilizzando math.sqrt(). 
Gestisci ValueError se l'input è negativo restituendo un messaggio informativo.'''

import math

def safe_sqrt (number):

    return math.sqrt(number)

try:
    prova = safe_sqrt(-5)

except ValueError as error:
    print(f"il numero è negativo, non verrà eseguito il programma: {error}")

else:
    print(prova)

