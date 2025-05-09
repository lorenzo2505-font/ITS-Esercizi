def count_isolated(mylist: list) -> int:
    contatore = 0
    
    
    for i in mylist:
        if mylist[0] != mylist[0 - 1] and mylist[i] != mylist[i - 1] and mylist[i] != mylist[i + 1] and mylist[-1] != mylist[-1 + 1]:
            contatore = contatore + 1
            
    return contatore
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))