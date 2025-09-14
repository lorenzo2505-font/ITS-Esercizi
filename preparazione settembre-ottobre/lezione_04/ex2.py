import random

'''2. Gioco "Indovina il numero":

Crea una funzione che genera un numero casuale all'interno di un intervallo specificato dall'utente.

Chiedi all'utente di indovinare il numero entro un numero massimo di tentativi specificato.

Fornisci un feedback all'utente dopo ogni tentativo, indicando se il suo tentativo è troppo alto, troppo basso o corretto.

Termina il ciclo quando l'utente indovina il numero correttamente o raggiunge il numero massimo di tentativi.'''


def indovinaNumero(intervallo: tuple[int], tentativi: int):
    
    if len(intervallo) != 2:
        
        raise ValueError("la tupla deve contenere due elementi")
    
    intervallo = sorted(intervallo)
    i = 0
    numero = random.randint(intervallo[0], intervallo[1])

    while i < tentativi:
        ques: int = int(input("inserisci numero: "))

        if ques < numero:
            print("troppo basso")
            i += 1

        elif ques > numero:
            print("troppo alto")
            i+=1
        
        else:
            print("indovinato")
            break


indovinaNumero((1, 10), 3)