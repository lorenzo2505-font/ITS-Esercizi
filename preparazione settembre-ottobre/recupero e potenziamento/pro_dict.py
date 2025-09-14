def proDict () -> dict:

    mydict: dict = {} # inizializzo un dizionario vuoto

    for x in range(100 + 1): # ciclo per ottenere tutti i valori necessari di x
        
        for y in range (2, 88 + 1, 2): # ciclo per ottenere tutti i valori necessari di y

            mydict[(x, y)] = x * y # aggiungo al dizionario la chiave (x,y) che ha come valore il prodotto tra le due variabili
    
    return mydict # restituisco il dizionario

d: dict = proDict() # inizializzo un dizionario tramite la funzione proDict

print(d[(13, 88)])

print(d[83, 56]) # faccio stampare i prodotti dei seguenti valori richiesti dalla traccia

print(d[71, 44])


        



