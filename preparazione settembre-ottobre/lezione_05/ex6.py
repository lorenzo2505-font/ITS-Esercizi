'''Utilizzare una list comprehension per creare una lista di tuple, ognuna contenente un numero e il suo quadrato.'''


mylist: list[tuple[int]] = [(x, x**2) for x in range(1, 10 + 1)]

print(mylist)

