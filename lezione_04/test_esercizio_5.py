'''Scrivi una funzione che rimuove tutti i duplicati da una lista,
 contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.'''

def remove_duplicates(mylist: list) -> list:
    for i in mylist:
        if mylist.count(i) != 0:
            pass
        else:
            mylist.remove(i)
    return mylist
print(remove_duplicates([1, 2, 3, 1, 2, 4]))
    
    


	





	

