'''Progettare un algoritmo che richieda all’utente di inserire un valore intero positivo n. 
Se nè negativo, il programma termina mostrando un messaggio di errore. Se n è positivo:

    l’utente può inserire 10 numeri interi;
    contare quanti di questi numeri sono divisibili per n.

Mostrare in output il risultato del conteggio.'''

n = int(input("inserisci un valore intero positivo: "))
i = 1
divisibili = 0
if n < 0:
    print("errore")
else:
    while i <=10:

        v = int(input("inserisci numero: "))
        i+=1
        if (n % v == 0):
            divisibili+=1
print(divisibili)



