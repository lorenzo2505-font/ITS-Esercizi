'''Generatore di numeri primi con il Crivello di Eratostene:

Crea una funzione che generi un elenco di numeri primi fino a un limite specificato utilizzando l'algoritmo del Crivello di Eratostene.

Inizializza un array di tutti i numeri fino al limite, contrassegnando inizialmente ogni numero come primo.

Scorri l'array partendo da 2 e contrassegna ogni multiplo del numero corrente come non primo.

I numeri rimanenti non contrassegnati sono i numeri primi entro il limite.
Restituisce l'elenco dei numeri primi.'''




def primes(r: int) -> list:

    contatore = 0

    mylist: list [int] = []

    for i in range(1, r + 1):

        mylist.append(i)
    
    for i in mylist:

        if i == 1:
            mylist.remove(i)

        else:

            for j in range(1, i):

                if i % j == 0:

                    contatore += 1
            
            if contatore <= 2:
                
                pass

            else: 
                mylist.remove(i)
                    

    
 
    return mylist



          

                            

                
            

print(primes(10))
