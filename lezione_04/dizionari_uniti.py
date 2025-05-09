def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key, value in  dict2.items():
        dict1[key] = value
        
            
            
            
        
        
        
    return dict1

print(merge_dictionaries({'x': 5}, {'x': -5}))

