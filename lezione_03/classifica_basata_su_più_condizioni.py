'''11. Classifica basata su più condizioni

Progettare un algoritmo che richieda all’utente di inserire un valore intero.
Il programma deve verificare:

se il numero è pari e maggiore di 10. Se sì, mostrare “Numero valido”;
se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”.

'''

n = int(input("inserisci numero: "))
if (n % 2 == 0) and (n > 10):
    print("numero  valido")
else:
    print("numero non valido")







