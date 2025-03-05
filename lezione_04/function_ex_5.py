'''Esercizio 5
Scrivi una funzione add_one(). Richiede un numero intero come argomento. La funzione aggiunge 1 al numero intero e lo restituisce.
Scrivi un'altra funzione add_one_to_list(). Richiede una lista di numeri interi come argomento.
Definire una variabile new_list in questa funzione.
Utilizzando un ciclo for, scorrere l'elenco degli argomenti.
Usando add_one(), riempi new_list con i numeri interi incrementati dall'elenco degli argomenti
entro 1.
Stampa nuova_lista.
Esempio:
aggiungi_uno_alla_lista([1, 2, 3])
stamperà:  [2, 3, 4]'''

def add_one(n: int):
    incremento = n + 1
    return incremento 

catch_n = add_one(n = int(input("inserisci numero: ")))
print(catch_n)

def add_one_list(in_list: list[int]):
    new_list:list = []
    for i in in_list:
        new_list.append(add_one(i))
    return new_list
catch_list: list[int] = [1, 2, 3]


print(add_one_list(catch_list))




    