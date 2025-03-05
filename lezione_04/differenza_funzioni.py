'''Proviamo a definire noi stessi una funzione chiamata sottrarre:
● Dovrebbero essere necessari 2 parametri.
● All'interno della funzione, dovrebbe sottrarre i due.
● Quindi, restituire il risultato.
Dopo averlo definito, chiama la funzione con alcuni argomenti!'''

def subtract(a: int, b: int):
    result = a - b
    return result
mysub = subtract(int(input("inserisci a: ")), int(input("inserisci b: ")))
print(mysub)

#test pazzo