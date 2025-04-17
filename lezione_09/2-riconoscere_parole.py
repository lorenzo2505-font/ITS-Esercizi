'''Obiettivo: Lavorare con lettere e lunghezze di stringhe.

    Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
    Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
    Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.
'''


import re 

mystr: str = "Pippo paperino naso"

risultato: list = re.findall(r"[A-z]{5,10}", mystr)

print(risultato)