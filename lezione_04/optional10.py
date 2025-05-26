'''Crea una funzione che verifichi se due stringhe date sono anagrammi l'una dell'altra.

Converti entrambe le stringhe in minuscolo e rimuovi tutti i caratteri non alfabetici.

Ordina i caratteri di ciascuna stringa e confronta le stringhe ordinate per verificarne l'uguaglianza.

Indica se le stringhe sono anagrammi o meno.'''




def anagrammi (mystr1: str, mystr2: str):


    mydict1: dict = {}

    mydict2: dict = {}


    mystr1 = sorted(mystr1)

    mystr2 = sorted(mystr2)

    
    for i in mystr1:

        mydict1[i] = mystr1.count(i)
    
    for i in mystr2:

        mydict2[i] = mystr2.count(i)
    
    
    if mydict1 == mydict2:

        return "le due parole sono anagrammi"
    
    else:

        return "le due parole non sono anagrammi"
    


print(anagrammi("lele", "elel"))

    

