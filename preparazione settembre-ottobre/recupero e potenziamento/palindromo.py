def recursivePalindrome(mystr: str):

    for i in mystr:
        
        if i.isupper():
            i = i.lower()
    
    mystr = mystr.replace(" ", "")

    if len(mystr) < 2:
        
        return True
    
    if mystr[0] != mystr[-1]:

        return False
    
    return recursivePalindrome(mystr[1:-1])



print(recursivePalindrome("anna"))