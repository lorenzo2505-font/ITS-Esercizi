'''Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.'''

def inverti_mappa(mydict: dict) -> dict:

    newdict: dict = {}

    for i in mydict:

        if i not in newdict:
            newdict[mydict[i]] = i
    
    return newdict


print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))

    