'''Esercizio 4
Scrivi una funzione check_each(), che accetta una lista di numeri come argomento.
Utilizzando un ciclo for, scorrere l'elenco.
Per ogni numero, stampa "più grande" se è maggiore di 5, "più piccolo" se è inferiore a 5 e "uguale" se è uguale a 5.'''

def check_each(mylist: list[int]): #definzione funzione
    for i in mylist:
        if i > 5:
            print(f"{i} è più grande di 5")
        elif i < 5:
            print(f"{i} è più piccolo di 5")
        else:
            print(f"{i} è uguale a 5")
catch_list: list[int] = [1, 2, 3, 4, 5, 6]
check_each(catch_list)        