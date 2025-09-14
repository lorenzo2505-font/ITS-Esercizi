'''2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''

def loopConditionalFun2(mylist: list[int], thresold: int) -> int:

    prodotto = 1

    for i in range(len(mylist)):

        if mylist[i] < thresold:
            prodotto *= mylist[i]
    
    return prodotto


l: list[int] = [x for x in range(1, 10 + 1)]

t: int = 5

print(loopConditionalFun2(l, t))




    