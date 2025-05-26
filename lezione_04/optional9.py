'''Cifratura/Decifratura con il Cifrario di Cesare

Crea funzioni per crittografare e decifrare un messaggio utilizzando il Cifrario di Cesare.

Consenti all'utente di specificare il valore di shift (numero di posizioni di cui spostare ogni lettera).

Gestisci sia la crittografia che la decifratura utilizzando la stessa funzione con gli opportuni adattamenti.

Crittografa e decifra il messaggio specificato utilizzando il valore di shift specificato.'''


#prima versione



def cesare (parola: str, shift: int ) -> str:

    




    

    critt: str = ""

    
    lettere: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "l", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

    '''for i in range(len(lettere)):

        if lettere[i] in parola:

            critt += lettere[i + 3]
    
    return critt'''

    for i in range(len(parola)):

        if parola[i] in lettere:

            for j in range(len(lettere)):

                if lettere[j] != parola[i]:

                    pass
                else:
                    critt += lettere[j + shift]

        

       
    
    return critt
            

        

  
    
    

            

        



            
    
    



'''t = cesare("cane", 3)'''





def decifra(critt: str, shift: int) -> str:


    dec: str = ""

    lettere: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "l", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]


    for i in range(len(critt)):

        if critt[i] in lettere:

            for j in range(len(lettere)):

                if lettere[j] != critt[i]:

                    pass
                else:
                    dec += lettere[j - shift]
    
    return dec


'''t2 = decifra (t, 3)


print(t2)'''



#seconda versione:


def cesarone (parola: str, shift: int, decrypt: bool = False):

    lettere: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "l", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

    critt: str = ""

    dec: str = ""


    if decrypt == True:


        for i in range(len(parola)):

            if parola[i] in lettere:

                for j in range(len(lettere)):

                    if lettere[j] != parola[i]:

                        pass
                    else:
                        critt += lettere[j + shift]
        return critt
    
    else:

        for i in range(len(parola)):

            if parola[i] in lettere:

                for j in range(len(lettere)):

                    if lettere[j] != parola[i]:

                        pass
                    else:
                        dec += lettere[j - shift]
        return dec
    


test = cesarone ("cane", 3)

print(test)


  
    


















