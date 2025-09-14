
def ricerca_binaria(mylist: list[int], n: int) -> bool:

    mylist = sorted(mylist) # ordino la lista

    if len(mylist) == 1: # se la lista ha un solo elemento controllo se quell'elemento corrisponde al numero n che sto cercando
        
        if n in mylist:
            
            return True
        
        else:
            
            return False
    
    elif len(mylist) == 0: # se la lista è vuota ritorno false
        
        return False
    
    else:
        inferior_index = 0 # indice inferiore della lista uguale a zero
        superior_index = len(mylist) - 1 # indice superiore della lista uguale alla lunghezza di essa meno 1
        mid = int((inferior_index + superior_index) / 2) # indice medio della lista uguale alla somma tra l'indice superiore e inferiore divisa per due

        if mylist[mid] > n: # se l'elemento al centro della lista è maggiore del numero n allora devo scorrere a sinistra
            # scorrere a sinistra
            return ricerca_binaria(mylist[:mid], n)
        
        elif mylist[mid] < n: # se l'elemento al centro della lista è minore del numero n allora devo scorrere a destra
            # scorrere a destra
            return ricerca_binaria(mylist[mid + 1:], n)
        
        else: # se invece è uguale ritorno subito True
            # trovato subito
            return True
    
    


lista = [x for x in range(1, 10 + 1)]

print(ricerca_binaria(lista, 11))





    