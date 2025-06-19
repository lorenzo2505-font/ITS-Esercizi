
def isDNA(mystr: str) -> bool:

    dna_list: list[str] = ["A", "C", "G", "T"]

    for i in mystr:

        if i in dna_list:

            continue
        
        else:

            return False
    
    return True




'''test = isDNA("CAGCTGATCGATGCTAGCCT")

print(test)'''


def sovrapposizioni(s1: str, s2: str):

    verify_s1 = isDNA(s1)

    verify_s2 = isDNA(s2)


    if verify_s1 == True and verify_s2 == True:

        pass




