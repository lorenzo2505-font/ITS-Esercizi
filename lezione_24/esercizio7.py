def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    newdict: dict = {}

    for key, value in dict1.items():

        if key in dict2:
            newdict[key] = dict1[key] + dict2[key]
        
        else:
            newdict[key] = value
    
    for key, value in dict2.items():

        if key not in dict1:
            newdict[key] = value
    
    return newdict