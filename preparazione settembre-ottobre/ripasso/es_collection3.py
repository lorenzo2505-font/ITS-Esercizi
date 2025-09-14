'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

def collectionFun3(mydict: dict[str, float]) -> dict[str, float]:

    newdict: dict[str, float] = {}

    for i in mydict:
        
        if mydict[i] < 50:
            newdict[i] = mydict[i] + mydict[i] * 10 / 100
    
    return newdict



d: dict[str, float] = {"cappello pierlions": 4.5, "canna del popa": 2.1, "aura del delisio": 999999.0}

print(collectionFun3(d))