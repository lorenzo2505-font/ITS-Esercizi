'''Generatore di numeri primi con il Crivello di Eratostene:

Crea una funzione che genera un elenco di numeri primi fino a un limite specificato utilizzando l'algoritmo del Crivello di Eratostene.
Inizializza un array di tutti i numeri fino al limite, contrassegnando inizialmente ogni numero come primo.
Esegui un'iterazione nell'array, partendo da 2, e contrassegna ogni multiplo del numero corrente come non primo.
I numeri rimanenti non contrassegnati sono i numeri primi entro il limite.
Restituisce l'elenco dei numeri primi.'''

import math

def eratostene(limit: int) -> list[int]:

    numbers: list[int] = [n for n in range(1, limit + 1)] # lista contenente i numeri da 1 fino al limite 
    possible_primes: list[bool] = [True for x in range(len(numbers))] # lista di booleani della stessa lunghezza delle precendente con tutti valori True (assumo inizialmente che tutti i numeri siano primi)
    primes: list[int] = []

    for i in range(int(math.sqrt(limit))): # itero fino alla radice quadrata del limite
        cont = 0 # per verificare che un numero sia primo inizializzo un contatore che poi aggiornerò in un ciclo while
        divisori = 0 # contatore che indica il numero di divisori del numero, al momento inizializzato a zero

        if numbers[i] < 2: # se il numero è minore di 2 (quindi 1) allora non è primo quindi metto possible_primes[i] a False
            possible_primes[i] = False
        
        else: # in alternativa verifico con un ciclo while che ogni numero sia primo
        
            while cont <= numbers[i]: # il ciclo si interrompe quando il contatore supera il valore del numero
                cont += 1 # aumento il contatore di 1

                if numbers[i] % cont == 0:
                    divisori += 1 # se la divisione tra il numero e il contatore non da resto allora il contatore è un divisore di quel numero e quindi il contatore dei divisori aumenta di 1
            
            if divisori > 2: # il il numero ha più di due divisori non è primo(un numero è primo solo se è divisibile per 1 e per se stesso) e quindi metto il corrispettivo possible_primes[i] a False
                possible_primes[i] = False
            
            else: # se invece il numero primo allora i suoi multipli non possono esserlo quindi avviene un secondo controllo

                for j in range(numbers[i], limit): # itero in un intervallo tra il numero e il limite(quest'ultimo non compreso nell'intervallo)
                    
                    if numbers[j] % numbers[i] == 0: # se la divisione tra numbers[j] e numbers[i] non da resto allora numbers[j] è multiplo nel numero primo numbers[i] e quindi imposto il corrispettivo possible_numbers[numbers[j] -1] a False (a meno che non lo sia già)
                        
                        if possible_primes[numbers[j] - 1]:
                            possible_primes[numbers[j] - 1] = False
                        
    
    for p in range(len(possible_primes)): # itero la lista di booleani
        
        if possible_primes[p]: # se possible_primes[p] ha valore True allora il corrispettivo numbers[p] è un numero primo e lo aggiungo alla lista contenenti i numeri primi
            primes.append(numbers[p])
    
    return primes # ritorno la lista contente i numeri primi


            
    
    
def main():

    print(eratostene(100))
    

main()


            
            
        

            
            




    
    
 

    
    
    