'''Scrivi una funzione che prenda in input una lista di dizionari 
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.'''

def aggrega_voti(mylist: list[dict]) -> dict[str, list[int]]:

    mydict: dict[str, list[int]] = {} # inizializzo un dizionario vuoto



    for i in range(len(mylist)): # ciclo la lista

        
        
        if mylist[i]["nome"] not in mydict: # se il nome dello studente non è del dizionario lo aggiungo con il suo corrispettivo voto all'interno di una lista
            mydict[mylist[i]["nome"]] = [mylist[i]["voto"]]
        
        else: # in caso contario aggiungo il nuovo voto alla lista
            mydict[mylist[i]["nome"]].append(mylist[i]["voto"]) 
    
    return mydict
            


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

