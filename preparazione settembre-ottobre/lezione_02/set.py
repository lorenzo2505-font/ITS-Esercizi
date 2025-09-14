


x = {"milano", "roma", "napoli"}

y = {"venezia", "udine", "roma"}

'''# ai set ci si accede tramite i cicli

# non si possono modificare gli elementi ma solo aggiungere e rimuovere

x.add("venezia") # aggiunge venezia

print(x)

x.update(y)

print(x) # aggiunge gli elementi di y a x

#rimuovere elementi

x.remove("venezia") # rimuove elementi all'interno del set

x.discard("udine") # anche se l'elemento non è presente nella lista il programma non da errore 


print(x)

# x.clear() pulisce il set del x cancella x'''

'''# utilizzare union(), update(), intersection()


z = x.union(y) # unisce i due elementi (escludono gli elemnti duplicati)

x.update(y) # aggiunge gli elementi di y a x

# union(): genera un nuovo set 

#update(): aggiorna il set su cui si sta lavorando

x.intersection_update(y) # restituisce solo gli elementi che hanno in comune, in questo caso roma

z = x.intersection(y) # restituisce un nuovo set con gli elementi in comune'''

print(x.union(y)) # stampa di due set uniti in uno escludendo le ripetizione

print(x.intersection(y)) # stampa gli elementi in comune tra i due set

print(x.difference(y)) # stampa gli elementi del primo set esclusi quelli che ha in comune con il secondo