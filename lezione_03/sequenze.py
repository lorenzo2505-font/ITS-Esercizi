'''19. Calcolo di sequenze condizionali

Scrivere un algoritmo che calcoli il valore di una sequenza numerica basata 
su un valore n inserito dall’utente. La sequenza segue queste regole:

se n è pari, calcolare la somma dei numeri da 1 a n che sono divisibili per 4;
se n è dispari, calcolare il prodotto dei numeri dispari da 1 a n;
se n è negativo, mostrare un messaggio di errore e terminare.
Infine, mostrare il risultato calcolato.

Soluzione:'''

n = int(input("lunghezza sequenza: "))
i = 1
somma = 0
prodotto = 1
while i <= n:
    i+=1
    if (n % 2 == 0) and (i % 4 == 0):
        somma = somma + i
        
        
    if (n % 2 != 0) and  (i % 2 != 0):
        prodotto = prodotto * i
        
    if n < 0:
        print("errore")
        break
print(somma)
print(prodotto)

