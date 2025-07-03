# ispirazione stack overflow 




def palindromo1(mystr: str) -> bool:

    mystr = mystr.lower().replace(" ", "")

    if len(mystr) < 2:

        return True # se la stringa ha meno di due caratteri la parola è palindroma
    
    if mystr[0] != mystr[-1]: # si la prima lettera è uguale la seconda l'esito è false 

        return False
    
    return palindromo1(mystr[1:-1]) # in alternativa richiamo la funzione dove metto come input la stringa dal secondo indice all'ultimo(non incluso nell'intervallo)





print(palindromo1("anna"))



        




    

    