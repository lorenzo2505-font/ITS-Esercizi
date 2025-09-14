'''Creare una list comprehension che genera i quadrati dei numeri da 1 a 10.'''

mylist: list[int] = [x**2 for x in range(1, 10 + 1)]

print(mylist)