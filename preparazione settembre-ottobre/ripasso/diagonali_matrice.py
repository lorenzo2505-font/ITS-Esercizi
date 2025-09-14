def sum_primary_diagonal(matrix: list[list[int]]):

    somma = 0
    num = 0

    for i in range(len(matrix)):
        
        if len(matrix[i]) != len(matrix):

            raise ValueError("la matrice deve essere di dimension n X n")
        
        somma += matrix[i][num]
        num += 1
    
    return somma

def sum_secondary_diagonal(matrix: list[list[int]]):

    somma = 0
    num = -1

    for i in range(len(matrix)):

        if len(matrix[i]) != len(matrix[i]):
            
            raise ValueError("la matrice deve essere di dimensioni n X n")
        
        somma += matrix[i][num]
        num -= 1
    
    return somma
    
        


mat1: list[list[int]] =  [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(sum_primary_diagonal(mat1))
print(sum_secondary_diagonal(mat1))