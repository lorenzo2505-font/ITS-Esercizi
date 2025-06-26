import random
# parte 1A


def genera(dim: int) ->list[list[int]]:


    matrix: list[list[int]] = []

    for r in range(dim):

        row: list[int] = []
    
        for c in range(dim):

            #row = random.sample(range(0,14), dim)

            while True:

                n = random.randint(0,13)
                
                if c == 0:

                    row.append(n)
                    break

                if n != row[0]:
                    row.append(n)
                    break

            

                
        matrix.append(row)
    
    
    
    
    return matrix




def printMAT(mymat: list[list[int]]):

    for r in range(len(mymat)):

        for c in range(len(mymat[r])):

            print(f"{mymat[r][c]:<5}", end = "")

        print("\n")




#t = genera(4)

#rintMAT(t)




def calcolaCarico(mymat: list[list[int]], r: int, c: int) -> int: 

    somma_righe = 0

    somma_colonne = 0
    

    for i in mymat[r]:

        somma_righe += i
    
    for i in range(len(mymat)):

        somma_colonne += mymat[i][c]
    
    carico = somma_righe - somma_colonne

    return carico


#print(calcolaCarico(t, 0 , 0))




def caricoNullo(mymat: list[list[int]]) -> list[tuple[int]]:



    nulls: list[tuple[int]] = []

    for r in range(len(mymat)):

        for c in range(len(mymat)):
            
            test = calcolaCarico(mymat, r, c)

            if test == 0:

                nulls.append((r, c))

    return nulls




#print(caricoNullo(t))


def caricoMax(mymat: list[list[int]]) -> tuple:

    max = 0

    

    for r in range(len(mymat)):

        for c in range(len(mymat)):

            test = calcolaCarico(mymat, r, c)

            if test > max:

                max = test
                
                mytuple = (r, c)

                
    print(max)
    return mytuple


#print(caricoMax(t))




def caricoMin(mymat: list[list[int]]):

    min= 0

    

    for r in range(len(mymat)):

        for c in range(len(mymat)):

            test = calcolaCarico(mymat, r, c)

            if test < min:

                min = test
                
                mytuple = (r, c)

                
    print(min)
    return mytuple


#print(caricoMin(t))




m = genera(5)

printMAT(m)


print(caricoNullo(m))


print(caricoMax(m))

print(caricoMin(m))




    

        

            

        
















    











    






    
    


