'''2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
'''


def collectionFun2(mylist: list[int]) -> dict:

    mydict: dict = {}
    pos_list: list[int] = []
    neg_list: list[int] = []

    for i in range(len(mylist)):

        if mylist[i] < 0:
            neg_list.append(mylist[i])
        
        else:
            pos_list.append(mylist[i])
    
    mydict["positivi"] = pos_list
    mydict["negativi"] = neg_list

    return mydict

l: list[int] = [x for x in range(-10,10)]

print(collectionFun2(l))