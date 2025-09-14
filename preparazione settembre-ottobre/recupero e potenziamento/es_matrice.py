import random

def genera(dim: int) -> list[list[int]]: # funzione che genera la matrice

    matrix: list[list[int]] = [] # creo la lista della matrice vuota

    for r in range(dim): # creo n righe basandomi sulla dimensione dim della matrice passata in input
        row: list[int] = [] # lista contenenti gli elementi della riga (al momento vuota)

        for c in range(dim): # creo n colonne basandomi sulla dimensione dim della matrice passata in input
            x: int = random.randint(0, 13) # creo il valora da inserire all'interno della matrice (casuale tra 0 e 13

            if not(row): # se la lista è vuota allora aggiungero un primo elemento alla riga
                row.append(x)
            
            else: # se non è così devo assicurarmi che i successivi elementi siano diversi dal primo
            
                while x == row[0]: # uso un ciclo while per modificare il valore di x nel caso l'n elemento sia uguale al primo che si interromperà solo in caso contrario alla seguente condizione
                    new_x: int = random.randint(0,13)
                    x = new_x
                
                row.append(x) # aggiungo x alla riga
        
        matrix.append(row) # aggiungo la riga alla matrice
    
    return matrix # restituisco la matrice
    

def printMAT(matrix: list[list[int]]): # funzione per stampare la matrice

    for r in range(len(matrix)):
        
        for c in range(len(matrix[r])):
            print(f"{matrix[r][c]:<5}", end = "")
        
        print("\n")

def calcolaCarico(matrix: list[list[int]], index_r: int, index_c: int): # funzione per calcolare il calico
    
    somma_riga = sum(matrix[index_r]) # variabile contenente il valore della somma degli elementi della riga specificata dall'indice passato in input
    somma_colonna = 0 # somma degli elementi della colonna inizializzata a zero
   

    for r in range(len(matrix)): # itero la matrice

        for c in range(len(matrix[r])): # itero ogni riga della matrice

            if c == index_c: # se l'indice c corrisponde a quello passato in input allora somma_colonna viene incrementato del valore matrix[r][c]
                somma_colonna += matrix[r][c]
    
    carico = somma_riga - somma_colonna # definisco la variabile carico uguale alla differenza tra la somma degli elementi di una riga e la somma degli elementi di una colonna
    
    return carico # ritorno il valore di caricod

def caricoNullo(matrix: list[list[int]]) -> list[tuple]:

    tuple_list: list[tuple] = [] # inizializzo una lista di tuple vuota

    for r in range(len(matrix)): # itero la matrice
        
        for c in range(len(matrix[r])): # itero la riga della matrice
            t = calcolaCarico(matrix, r, c) # variabili t uguale al valore della funzione calcolaCarico() in cui sono passati in input la matrice, l'attuale indice r e l'attuale indice c 
            
            if t == 0: # se il valore t (quindi il risultato del carico) è zero aggiungo alla lista una tupla contenente l'indice della riga e della colonna
                tuple_list.append((r, c))
    
    return tuple_list # ritorno la lista

def caricoMax(matrix: list[list[int]]) -> tuple: # funzione per calcolare il carico con il valore più alto

    max = False # variabile max inizializzata a False (0)

    for r in range(len(matrix)): # itero la matrice

        for c in range(len(matrix[r])): # itero la riga della matrice
            t = calcolaCarico(matrix, r, c) # variabile t uguale al valore della funzione calcolaCarico() in cui sono passati in input la matrice, l'attuale indice r e l'attuale indice c 

            if t > max or max is False: # se t è più grande del valore massimo o è false(0) allora il valore di max è uguale a quello di t e definisco una tupla contenente gli indici r e c
                max = t
                max_tuple: tuple = (r, c)
    
    return max_tuple

def caricoMin(matrix: list[list[int]]):  # funzione per calcolare il carico con il valore più basso (stesso procedimento con caricoMin ma nel condizionale si usa il segno < anzichè >)

    min = False

    for r in range(len(matrix)):

        for c in range(len(matrix[r])):
            t = calcolaCarico(matrix, r, c)

            if t < min or min is False:
                min = t
                min_tuple: tuple = (r, c)
    
    return min_tuple





def main():

    popa = genera(5)
    printMAT(popa)

    print(caricoNullo(popa))
    print(caricoMax(popa))
    print(caricoMin(popa))

main()


    
    
    

