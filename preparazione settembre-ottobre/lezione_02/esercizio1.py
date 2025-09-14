'''scrivere una funzione che accetti una lista di interi

e restituisca una lista di tuple, dove ogni tupla contenga l'elemento e il suo indice nella lista originale

esempio: [4, 5, 6, 7] -> [(4, 0), (5, 1), (6,2), (7,3)]'''


def myfun1 (mylist: list[int]) -> list[tuple[int]]:

    tuple_list: list[tuple[int]] = []

    for i in range(len(mylist)):

        tuple_list.append((mylist[i], i))
    
    return tuple_list


l: list[int] = [4, 5, 6, 7]

print(myfun1(l))