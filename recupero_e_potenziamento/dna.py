
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

        ind1 = -1

        ind2 = 0

        while True:

            if s1[ind1] != s2[0]:

                ind1 -= 1
                ind2 += 1

            elif s1 == s2:

                print("le due suquenze sono uguali")
                print(len(s1))
                break    
            
            else:

                if s1[ind1: ] == s2[:ind2 + 1]:

                    print("sovrapposizione trovata")

                    print(f"fine prima stringa: {s1[ind1: ]}")

                    print(f"inizio seconda stringa: {s2[:ind2 + 1]}")

                    print(f"lunghezza sovrapposizione: {len(s1[ind1: ])}")
                    break

                else:

                    ind1 -= 1

                    ind2 +=1




