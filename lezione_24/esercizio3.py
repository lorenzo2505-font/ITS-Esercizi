def frequency_dict(elements: list) -> dict:
    mydict: dict = {}

    for el in elements:

        if el not in mydict:
            mydict[el] = 1
        
        else:
            mydict[el] += 1
    
    return mydict