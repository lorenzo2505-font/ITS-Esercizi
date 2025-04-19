'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''

'''esempio [('a', 1), ('b', 2), ('a', 3)] -> {'a': [1, 3], 'b': [2]}'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    
    mydict: dict = {}

    for i in len(tuples):
        tuples.count(i)
        mydict[i] = mydict[i+1]
    
    return mydict

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
    

    





