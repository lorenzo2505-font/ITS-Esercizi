'''scrivere una funzione che accetti una lista di interi e restituisca il numero di elementi pari presenti nella lista

es: [1, 2, 3, 4, 5] -> 2'''


def myfun3(mylist: list[int]) -> int:

    counter = 0

    for i in range(len(mylist)):

        if mylist[i] % 2 == 0:

            counter += 1
    
    return counter

l: list[int] = [1, 2, 3, 4, 5]

print(myfun3(l))

