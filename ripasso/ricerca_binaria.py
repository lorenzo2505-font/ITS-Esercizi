'''Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.'''









def bin_search(mylist: list [int], n: int):


    orderedList: list [int] = sorted(mylist)


    c = orderedList[int(len(orderedList) / 2) - 1]


    tentativi = 0

    print(c)

    
    while True:

        if orderedList[c - 1] == n:

            return True
        
        else:

            tentativi += 1

            if orderedList[c -1] < n:

                for i in orderedList[c:]:

                    if i > c:

                        c = i

                        print(c)

                        break
            
            elif orderedList[c -1 ] > n:

                for i in orderedList[:c]:
                    

                    if i < c:

                        c = i

                        print(c)

                        



                        break
        
        if tentativi == len(orderedList):

            return False


                    

    

            




test = bin_search([1, 2, 3, 4], 4)


print(test)




#versine prof



intList: list[int] = [2, 3, 5, 7, 10, 15, 42]


def binSearchProf(x: list [int], y: int):

    x = sorted(x)

    mid = len(x) // 2

    i = 0

    j = -1


    if x[mid] == y:

        print("numero trovato")

    elif x[mid] > y:

        j = mid 


        binSearchProf(x[i:j], y)
    
    else:

        i = mid + 1

        binSearchProf(x[i: j], y)





# altra mia versione



def otherBin(mylist: list [int], n: int):


    mylist = sorted(mylist)


    c = (len(mylist) // 2) - 1


    while True:

        if mylist[c - 1] == n:

            return True
        
        
        else:

            if mylist[c - 1] < n:

                for i in mylist[c:]:

                    if i == n:

                        return True
            
                return False

            elif mylist[c - 1] > n:

                for i in mylist[:c]:

                    if i == n:

                        return True
                
                return False
            



other = otherBin([1, 2, 3, 4], 5)


print(other)



        

