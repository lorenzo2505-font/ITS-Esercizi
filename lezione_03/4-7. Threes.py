'''Crea un elenco dei multipli di 3, da 3 a 30. Utilizza un ciclo for per stampare i numeri nell'elenco.'''


mylist: list[int] = []

for i in range(3, 30 +1):

    if i % 3 == 0:
        
        mylist.append(i)

print(mylist)


