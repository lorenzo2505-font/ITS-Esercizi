'''6-2. Numeri preferiti: utilizza un dizionario per memorizzare i numeri preferiti delle persone.
Pensa a cinque nomi e usali come chiavi nel tuo dizionario. Pensa a un numero preferito per ogni persona e memorizza ciascuno come valore nel tuo dizionario.
 Stampa il nome di ogni persona e il suo numero preferito. Per divertirti ancora di più, invia un sondaggio ad alcuni amici e ottieni alcuni dati reali per il tuo programma.'''

numeri_preferiti: dict = {"Lorenzo": 25, "Roberta": 22, "Antonio": 100, "Francesco Totti": 10, "Daniele De Rossi": 16}
for key, value in numeri_preferiti.items():
    print(key, value)


