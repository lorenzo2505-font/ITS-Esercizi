
def sequenza(x: int):

    seq: list[int] = [] # inizializzo la sequenza con una lista vuota
    posizione = None # inizializzo la variabile posizione con momentaneo valore None
    somma = 0 # inizializzo la variabile somma con valore momentaneo 0

    while type(x) != int or x < 0: # se x non è intero o è negativo chiedo all'utente di inserirlo di nuovo
        x = int(input("inserisci un valore di x intero positivo: ")) 
    
    while True: # ciclo infinito
        n = int(input("inserisci un numero intero positivo: "))

        if type(n) == int and n >= 0: # se il numero è negativo o non intero non lo considero non aggiungendolo alla sequenza
            seq.append(n)
        
        if n == 0: # se il numero è zero esco dal ciclo
            break
    
    for i in range(len(seq)): # ciclo la sequenza

        if seq[i] == x: # controllo se l'elemento della sequenza è uguale a x

            while posizione == None: # se la posizione ha un valore nullo le assegno il valore dell'indice del primo elemento uguale ad x
                posizione = i
        
        else:
            somma += seq[i] # qualsiasi elemento diverso da x verrà sommato
    
    print(seq) # stampo la sequenza

    print(f"il numero {x} appare {seq.count(x)} volte all'interno della sequenza") # con la funzione count conto quante volte x appare nella sequenza

    print(f"il numero {x} appare per la prima volta nella posizione {posizione} all'interno della sequenza") # stampo la prima posizione di x

    print(f"la somma dei valori della sequenza diversi da {x} è {somma}") # stampo la somma della sequenza con i valori di x esclusi

    



sequenza(3)


    
        
        
        
        
    


