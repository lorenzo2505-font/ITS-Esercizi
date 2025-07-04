def baricentro(v: list[int]) -> int|None:

    i = 0

    while i < len(v):

        if sum(v[:i + 1]) == sum(v[i + 1:]):

            return i
        
        else:

            i += 1
    
    return None








def printResult(v: list[int]):

    res = baricentro(v)


    if res == None:

        print(f"Il baricentro del vettore v={v} non esiste!")
    
    else:

        print(f"Esiste il baricentro del vettore v={v} ed è dato dall'indice i={res}!")







def baricentroOttimizzato(v: list[int]):

    somma = 0

    ind = 0

    for i in range(len(v)):

        somma += v[i]
    
    
    while ind < len(v):

        somma_sinistra = sum(v[:ind + 1])

        somma_destra = somma - somma_sinistra

        if somma_destra == somma_sinistra:

            return ind
        
        else:

            ind += 1
        
    return None



v1: list[int] = [1, 2, 3, 2, 5, 2, 1]

v2: list[int] = [2, 0, -1, 4, 6, 3, -1]


printResult(v1)

printResult(v2)



print(baricentroOttimizzato(v1))

print(baricentroOttimizzato(v2))




    




    