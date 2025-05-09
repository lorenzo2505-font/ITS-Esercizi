'''4-5. Sommare un milione: crea un elenco dei numeri da uno a un milione, quindi utilizza min() e max() 
per assicurarti che l'elenco inizi effettivamente da uno e termini con un milione.
 Inoltre, usa la funzione sum() per vedere quanto velocemente Python può aggiungere un milione di numeri.'''

mylist: list[int] = []

for i  in range(1, 1000000 + 1):
    mylist.append(i)
    
print(max(mylist))
print(min(mylist))
print(sum(mylist))
