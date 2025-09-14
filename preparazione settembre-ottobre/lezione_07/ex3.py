'''Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.'''

def rimuovi_elementi(mylist: list[int], mydict: dict[int, int]):

    for i in mydict:
        
        for j in range(mydict[i]):

            if i in mylist:
                mylist.remove(i)
    
    return mylist

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))