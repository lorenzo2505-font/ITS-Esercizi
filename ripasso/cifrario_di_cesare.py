'''Cifrario di Cesare
Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste
a chi non possiede la chiave per decifrarle.
Immagina l’alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere
dell’alfabeto minuscole scrivendo from string import ascii_lowercase
Ogni lettera ha una posizione in questa lista:
● a è 1
● b è 2
● j è 10
● e così via…
Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero
positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
alla posizione della lettera cifrata.





● a con key = 2 diventa c
Se la chiave porta oltre la fine dell’alfabeto, si ricomincia dal principio:
● a con key = 28 diventa c
Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
all’indietro nell’alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:
● s è una stringa (lettera, parola, frase, ecc.).
● key è un numero intero positivo, la chiave del cifrario di Cesare.
La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.
Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o
decifrata.'''


from string import ascii_lowercase

from string import ascii_uppercase




def caesar_cypher_encrypt(s: str, key: int) -> str:


    alfabetoLower = ascii_lowercase

    alfabetoUpper = ascii_uppercase

    

    


    parolaEncriptata = ""

    if key < 0:

        raise ValueError("la chiave non può avere valore negativo")
    
    if key > 26:

        key -= 26
    


    for i in range(len(s)):

        if s[i] in alfabetoLower:

            for j in range(len(alfabetoLower)):

                if alfabetoLower[j] == s[i]:

                    parolaEncriptata += alfabetoLower[j + key]
        
        elif s[i] in alfabetoUpper:

            for z in range(len(alfabetoUpper)):


                if alfabetoUpper[z] == s[i]:

                

                    parolaEncriptata += alfabetoUpper[z + key]
        
        else:

            parolaEncriptata += s[i]

            

            
    

    return parolaEncriptata



e = caesar_cypher_encrypt("cAne#1è", 3)


print(e)




def caesar_cypher_decrypt(s: str, key: int) -> str:


    alfabetoLower = ascii_lowercase

    alfabetoUpper = ascii_uppercase


    parolaDecriptata = ""


    if key < 0:

        raise ValueError("la chiave non può avere valore negativo")
    
    if key > 26:

        key -= 26
    


    for i in range(len(s)):

        if s[i] in alfabetoLower:

            for j in range(len(alfabetoLower)):

                if alfabetoLower[j] == s[i]:

                    parolaDecriptata += alfabetoLower[j - key]
        
        elif s[i] in alfabetoUpper:

            for z in range(len(alfabetoUpper)):

                if alfabetoUpper[z] == s[i]:

                    parolaDecriptata += alfabetoUpper[z - key]
        
        else:


            parolaDecriptata += s[i]
    
    return parolaDecriptata




d = caesar_cypher_decrypt(e, 3)


print(d)


# versione prof



def cesare(x, k):

    l = ""

    for c in x:


        idx = ascii_lowercase.index(c)

        new_idx = (idx + k) % 26 

        new_char = ascii_lowercase[new_idx] 

        l += new_char














