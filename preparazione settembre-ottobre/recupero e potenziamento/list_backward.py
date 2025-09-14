def printListBackward(mylist: list):

    if not(mylist):

        return
    
    else:
        print(mylist[-1])
        printListBackward(mylist[:-1])
       

        

printListBackward([x for x in range(10)])


