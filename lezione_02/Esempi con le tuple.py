my_touple= (10, 20, 30)
print(my_touple[0]) #uso l'indexing
print(my_touple[1: ])#slicing
second_touple= (1, "strings", 4.5, True, 4.5)
print(second_touple[1])
print("\n" + str(type(my_touple))) #prova che sia una tupla
print(my_touple.count(4.5)) #numero occorrenza
print(my_touple.index("strings"))