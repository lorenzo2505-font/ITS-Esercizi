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


                    

    

            




test = bin_search([1, 2, 3, 4], 5)


print(test)