def baricentro(v: list[int]) -> int|None:

    index = 0 # inizializzo il valore di index che farà da indice per gli elementi all'interno del vettore

    while index < len(v): # se il valore dell'indice è maggiore o uguale alla lunghezza del vettore allora non vi è un baricentro ed esco dal ciclo

        if sum(v[:index + 1]) == sum(v[index + 1:]): # se la somma dal lato sinistro è uguale alla somma dal lato destro allora vi è un baricentro e restituisco il valore di index
            
            return index
        
        else: # se le due somme non sono uguali incremento di 1 il valore dell'indice 
            index += 1
    
    return None # se non vi è un baricentro restituisco None


l: list[int] = [1, 2, 3, 3, 2, 1]


def printResult(v: list[int]): # funzione che in base al risulatato di una delle due funzioni sul baricentro stampa un determinato messaggio

    res = baricentro(v)

    if res is not None:
        print(f"Esiste il baricentro del vettore v={v} ed è dato dall'indice i={res}!")
    
    else:
        print(f"Il baricentro del vettore v={v} non esiste!")



def baricentroOttimizzato(v: list[int]) -> int|None:

    somma = 0 # inizializzo a 0 il valore della somma
    index = 0 # inizializzo il valore di index che farà da indice per gli elementi all'interno del vettore

    for i in range(len(v)): # ciclo tutto il vettore per ottenere la somma
        somma += v[i]
    
    while index < len(v): # se il valore dell'indice è maggiore o uguale alla lunghezza del vettore allora non vi è un baricentro ed esco dal ciclo
        somma_sinistra = sum(v[:index + 1]) # faccio la somma sul lato sinistro aiutandomi col valore di index
        somma_destra = somma - somma_sinistra # ottengo la somma sul lato destro facendo la differenza tra la somma totale e la somma sul lato sinistro

        if somma_sinistra == somma_destra: # se le due somme sono uguali vi è un baricentro e restituisco il valore di index
            
            return index
        
        else: # se le due somme non sono uguali allora incremento il valore di 1
            index += 1
    
    return None # se non vi è un baricentro restituisco None

print(baricentroOttimizzato(l))
    




        

        





