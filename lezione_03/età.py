'''Progettare un algoritmo che richieda all’utente di inserire la sua età.
L'algoritmo deve:

controllare se l’età è compresa tra 18 e 65 anni. 

Se sì, mostrare un messaggio che indica che l’utente può partecipare all’attività;
se l’età non rientra nell’intervallo, verificare se è inferiore a 18 oppure maggiore di 65.
 Se sì, mostrare un messaggio che indica che l’utente non può partecipare perché ha
   superato l'età massima consentita o non ha raggiunto l'età minima consentita.
'''
età = int(input("inserisci l'età: "))
if (età >= 18) and (età <= 65):
    print("puoi partecipare all'attività")
if (età < 18):
    print("non puoi partecipare all'attività, sei minorenne")
if (età > 65):
    print("non puoi partecipare  all'attività, sei Over 65")
    
