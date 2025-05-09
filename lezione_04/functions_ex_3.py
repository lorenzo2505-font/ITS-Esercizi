'''Esercizio 3
Scrivi una funzione print_numbers(), che accetta una lista di numeri come argomento.
Usando un ciclo for, stampa ogni numero uno per uno'''

def print_numbers(mylist: list[int]): #definzione funzione
    for i in mylist:
        print(i)
catch_list: list = [1, 2, 3, 4, 5]
print_numbers(catch_list) #invocazione funzione


