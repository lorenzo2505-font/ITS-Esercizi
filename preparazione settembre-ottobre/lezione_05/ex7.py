'''Scrivere una list comprehension che filtra i numeri dispari di una lista e calcola il cubo di ciascuno.'''

numbers: list[int] = [x for x in range(10)]

mylist: list[int] = [i**3 for i in numbers if i % 2 != 0]

print(mylist)