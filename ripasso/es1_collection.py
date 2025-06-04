''') Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.'''


# mia soluzione

def fun(mylist: list[tuple]) -> dict:

    mydict: dict = {}


    for i in range(len(mylist)):

        mydict[i] = mylist[i]

        

        
    
    return mydict


t = fun([(1, 2)])

print(t)



#soluzione prof


def funProf(lista: list[tuple]) -> dict:

    dizionario1: dict = {}

    

    for element in lista:

        key, value = element[0], element[1]

        if key in dizionario1:

            dizionario1 [key] += value
        
        else:

            dizionario1[key] = value
    
    return dizionario1




test = funProf([(1, "a"), (2, "b"), (3, "c")])

print(test)





        

    

