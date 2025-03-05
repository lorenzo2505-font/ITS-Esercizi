'''6-10. Numeri preferiti: modifica il tuo programma dell'esercizio 6-2 in modo che ogni persona possa avere più di un numero preferito. 
Quindi stampa il nome di ogni persona insieme ai suoi numeri preferiti.'''


numeri: dict = {
    "Lorenzo": {
        "primo numero" : 25,
        "secondo numero" : 21

    },
    "Roberta" : {
        "primo numero" : 22,
        "secondo numero" : 119
    },
    "Antonio" : {
        "primo numero" : 100,
        "secondo numero" : 1

    },

    "Francesco Totti" : {
        "primo numero" : 10,
        "secondo numero" : 8
    },
    "Daniele De Rossi": {
        "primo numero": 16,
        "secondo numero": 9
    }
}

for  key, value in numeri.items():
    print(key, value)