stringa = "ArCObaLeNO"

def uppercase (stringa):
    
    # CASO BASE
    if stringa == "":
        print("")
    
    elif stringa[0] == stringa[0].upper():
        print(stringa[0], end="") # per stampare tutto sulla stessa riga
        uppercase(stringa[1: ])
    
    else:
        uppercase(stringa[1: ])

uppercase("PROGrammarePYthOn")


    