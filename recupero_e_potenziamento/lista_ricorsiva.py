newlist = []
def printListBackward(mylist: list):

    

    if len(mylist) == 0:

        return newlist
    
    else:

        newlist.append(mylist[-1])

        mylist.remove(mylist[-1])

        return printListBackward(mylist)




print(printListBackward([1, 2, 3, 4, 5]))

    

        







