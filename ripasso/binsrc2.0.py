lista: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binsrcMine(mylist: list[int], n: int):

    if len(mylist) == 0:  

        return False
    
    if len(mylist) == 1:  

        return mylist[0] == n
    
    else:

        lowInd = 0

        upInd = len(mylist) - 1

        mid = int((lowInd + upInd) / 2)
        
        if mylist[mid] == n:  

            return True
        
        elif mylist[mid] > n:
            

            return binsrcMine(mylist[:mid], n)  # chiamata della funzione
        
        else:

            return binsrcMine(mylist[mid + 1:], n)  # chiamata della funzione




test = binsrcMine(lista, 11)

print(test)  # Ora stampa True

