'''creare una funzione,
che accetti una lista di stringhe, 
e restituisca un dizionario dove le chiavi sono le stringhe,
e i valori sono il numero di volte in cui una stringa appare nella lista

es: [ciao, mondo, ciao, mondo, mondo] -> {ciao: 2, mondo: 3}'''

def myfun2(mylist: list[str]) -> dict[str, int]:

    mydict: dict[str, int] = {}

    for i in range(len(mylist)):

        mydict[mylist[i]] = mylist.count(mylist[i])
    
    return mydict

l = ["ciao", "mondo", "ciao", "mondo", "mondo"]

print(myfun2(l))


# metodo alternativo

def alternative_fun2(mylist: list[str]) -> dict[str, int]:

    mydict: dict[str, int] = {}

    for i in range(len(mylist)):

        if mylist[i] in mydict:

            mydict[mylist[i]] += 1
        
        else:

            mydict[mylist[i]] = 1
        
    return mydict


print(alternative_fun2(l))


    
