'''scrivere una funzione che accetti una lista di interi
e restituisca una lista di interi contenenti solo numero divisibili per 3

es: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [3, 6, 9]'''

def myfun4(mylist: list[int]) -> list[int]:

    three_list: list[int] = []

    for i in range(len(mylist)):

        if mylist[i] % 3 == 0:

            three_list.append(mylist[i])
    
    return three_list


l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(myfun4(l))