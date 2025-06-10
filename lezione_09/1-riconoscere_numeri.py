'''1. Riconoscere numeri

Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

    Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
    Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).
'''
import re
mystr: str = "ho 20 anni, sono alto 186 centimetri, sto facendo un corso dalla durata di 2 anni, esempio di numero negativo: -1"





result = re.findall(r"[0-9]+", mystr)






result2 = re.findall(r"-[0-9]+", mystr)

print(result)

print(result2)




