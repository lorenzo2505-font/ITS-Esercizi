def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    mydict: dict[str, list[str]] = {}

    for i in range(len(tuples)):

        if tuples[i][0] not in mydict:
            mydict[tuples[i][0]] = [tuples[i][1]]
        
        else:
            mydict[tuples[i][0]].append(tuples[i][1])
    
    return mydict

