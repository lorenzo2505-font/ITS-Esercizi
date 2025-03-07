#valori di default

def total (w, x, y = 10, z = 20):
    return(w ** x) + y + z
#chiamata totale della funzione omettendo gli ultimi due valori

total(2, 3) #output 38

#chiamata totale di funzione, omettendo l'ultimo valore

total(2, 3, 4) #output 32

#chiamata totale della funzione senza omettere valori

total(2, 3, 4, 5)

