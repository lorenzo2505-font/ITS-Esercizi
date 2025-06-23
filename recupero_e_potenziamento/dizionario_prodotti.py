def proDict() -> dict[tuple[int], int]:

    mydict: dict[tuple[int], int] = {}

    mylist1: list[int] = [x for x in range(0, 100 + 1)]

    mylist2: list[int] = [x * 2 for x in range(1, 44 + 1)]

    

    for i in range(len(mylist1)):

        for j in range(len(mylist2)):

            mydict[(mylist1[i], mylist2[j])] = mylist1[i] * mylist2[j]
    
    
    return mydict


test = proDict()


print(test[13, 18])



print(test[83, 56])



print(test[71, 44])









