def riordina(mylist: list[int]) -> list[int]:
    newlist: list[int] = []
    
    while True:
        minimo = mylist[0]
        
        for i in mylist:
            
            if i < minimo:
                minimo = i
        
        newlist.append(i)
        mylist.remove(i)
        
        if not(mylist):
            break
    
    return newlist


if __name__ == '__main__':

    print(riordina([5, 4, 3, 2, 1]))