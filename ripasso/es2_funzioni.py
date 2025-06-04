'''Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold'''


def fun(mylist: list[int], threshold: int) -> int:

    mult: int = 1

    for i in mylist:

        if i < threshold:

            mult = mult * i
    
    return mult

t = fun([2, 4, 5, 8], 7)


print(t)


def fattorialeRicorsivo(n):

    if n <= 0:

        return "errore"
    
    elif n == 1:

        return 1
    
    else:

        return n * fattorialeRicorsivo(n - 1)



ric = fattorialeRicorsivo(5)

print(ric)




