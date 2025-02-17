'''12. Scelta condizionale basata su input multipli

Progettare un algoritmo che richieda all’utente di inserire un numero variabile n di valori x e y.
 L'algoritmo deve:

calcolare il prodotto di x e y solo se entrambi i valori sono positivi;
calcolare la somma di x e y solo se uno dei due valori è negativo;
mostrare il risultato dell’operazione effettuata o un messaggio di errore altrimenti.'''

n = int(input("quante coppie di valori x ed y vuoi inserire ?: "))
i = 1
while i <= n:
    x = int(input("inserisci x: "))
    y = int(input("inserisci y: "))
    i+=1
    if (x > 0) and (y > 0):
        prodotto = x * y
        print(prodotto)
    if (x > 0) and (y < 0):
        somma = x  +  y
        print(somma)
    if (x < 0) and (y > 0):
        somma = x + y
        print(somma)
    if (x < 0) and (y < 0):
        print("errore")

