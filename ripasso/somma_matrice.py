'''Somma delle Diagonali di una Matrice (Quadrata o
Rettangolare)

Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:

1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).

2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).

Requisiti:
● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.
Esempi:
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15

sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15'''




def sum_primary_diagonal(mylist: list [list[int]]) -> int:


    somma = 0

    x = 0

    

    for i in range(len(mylist)):

        if len(mylist[i]) != len(mylist):

            raise Exception("la matrice deve essere di dimensioni n X n")

        

        somma += mylist[i][x]

        x += 1
    
    return somma



test = sum_primary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(test)




def sum_secondary_diagonal(mylist: list[list[int]]) -> int:

    somma = 0

    x = -1


    for i in range(len(mylist)):

        if len(mylist[i]) != len(mylist):

            raise Exception("la matrice deve essere di dimensioni n X n")

        somma += mylist[i][x]

        x -= 1
    
    return somma





secondTest = sum_secondary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


print(secondTest)




# versione prof





def matrixProf(x: list[list[int]]):

    somma = 0

    somma2 = 0

    for i in range(len(x)):

        somma += x[i][i]


        somma2 += x[i] [len(x) -1 - i]


    return somma, somma2





