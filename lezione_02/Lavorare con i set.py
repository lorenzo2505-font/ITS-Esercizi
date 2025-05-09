list_with_duplicates = [1, 2, 1, 3]
no_duplicates = set(list_with_duplicates) #casting lista-set
float("123") #altro tipo di casting 
set_a = {1, 2, 3,  4, 5}
set_b = {4, 5, 6, 7, 8}
set_a.add(6) #aggiunge un numero ad a 
print(set_a)
set_a.remove(2) #rimuve un numero da a 
print(set_a)
print(set_a.union(set_b)) #fa l'unione, insiemistica 
print (set_a | set_b) #|=or unione 
print(set_a.intersection(set_b)) #fa l'intersezione insiemistica
print(set_a & set_b) #&=and intersezione
print(set_a.difference(set_b)) #fa una sorta di differenza 
print(set_a - set_b) #-=minus differenza
