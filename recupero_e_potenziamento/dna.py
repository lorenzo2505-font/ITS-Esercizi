
def isDNA(mystr: str) -> bool:

    dna_list: list[str] = ["A", "C", "G", "T"]

    for i in mystr:

        if i in dna_list:

            continue
        
        else:

            return False
    
    return True







def sovrapposizioni(s1: str, s2: str):

    verify_s1 = isDNA(s1)

    verify_s2 = isDNA(s2)


    if verify_s1 and verify_s2:

        ind1 = -1

        ind2 = 0

        s_vuota = " "

        while True:

            if s1[ind1] != s2[0]:

                ind1 -= 1
                ind2 += 1

            elif s1 == s2:

                print("sovrapposizione trovata")
                print(s1)
                print(s2)

                return f"sovrapposizione massima: {len(s2)}"   
            
            else:

                if s1[ind1: ] == s2[:ind2 + 1]:

                    print("sovrapposizione trovata")
                    print(s1)
                    print(f"{s_vuota * len(s1[ind1: ])}{s2}")

                    return f"sovrapposizione massima: {len(s1[ind1: ])}"


                else:

                    ind1 -= 1

                    ind2 +=1


            if abs(ind1) > len(s1):

                print("sovrapposizione non trovata")

                return f"sovrapposizione massima: {0}"














