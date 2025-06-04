'''Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''



def fun(mydict: dict[str, float]) -> dict[str, float]:

    newdict: dict = {}

    for key, value in mydict.items():

        if value >= 50.0:
            
            continue 
        
        else:

            newdict[key] = round(value + (value * 10 / 100), 2)
    
    return newdict

t = fun({"banana": 55.0, "mela": 40.0})

print(t)



#soulzione prof


def funProf(dict_1: dict) -> dict:

    dict_new: dict = {}

    pass