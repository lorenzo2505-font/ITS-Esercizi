from string import punctuation
def count_unique_words(text: str) -> dict:
    
    lower_text = text.lower()
    mydict: dict = {}
    p = punctuation

    for i in lower_text.split(" "):
        
        if i.strip(p) not in mydict:
            mydict[i.strip(p)] = 1
        
        else:
            mydict[i.strip(p)] += 1
    
    return mydict
    
    



print(count_unique_words("Hello, world! Hello... PYTHON? world."))