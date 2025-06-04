''' Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''


#soluzione mia


def fun(mylist: list[int]) -> dict:

    mydict: dict = {}

    positivi: list[int] = []

    negativi: list[int] = []


    for i in range(len(mylist)):

        if mylist[i] >= 0:

            positivi.append(mylist[i])
        
        else:

            negativi.append(mylist[i])
    
    mydict["numeri postivi"] = positivi

    mydict["numeri negativi"] = negativi

    return mydict


t = fun([1,-2, 5])

print(t)




#soluzione prof


def funProf(lista: list[float|int]) -> dict[str, list|int]:

    dizionario_1: dict[str, list[int|float]] = {"positivi": [], "negativi": []}

    for element in lista:

        if element >= 0:

            dizionario_1["positivi"].append(element)
        
        else:

            dizionario_1["negativi"].append(element)
    
    return dizionario_1



