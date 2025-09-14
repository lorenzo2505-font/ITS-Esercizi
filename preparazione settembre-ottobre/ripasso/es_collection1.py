'''1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.'''

def collectionFun1(mylist: list[tuple]) -> dict:

    mydict: dict = {} # inizializzo un dizionario vuoto

    for i in range(len(mylist)): # ciclo la lista

        if len(mylist[i]) != 2: # ogni tupla deve contenere una chiave e un valore quindi due elementi in totale, in caso contrario mando il programma in errore
            
            raise ValueError("ogni tupla deve contenere 2 elementi")
        
        for j in range(len(mylist[i])): # ciclo la tupla 

            if mylist[i][j] not in mydict: # se la chiave della tupla non è nel dizionario la aggiungo con il rispettivo valore

                mydict[mylist[i][j]] = mylist[i][j + 1]
                break
            
            else: # in caso contrario sommo il nuovo valore con quello precedente

                v = mydict[mylist[i][j]] + mylist[i][j + 1]
                
                mydict[mylist[i][j]] = v
                break
    
    return mydict


l: list[tuple] = [("alessandro", "popa"), ("alessandro", "colella"), ("lorenzo", "rossi")]



print(collectionFun1(l))