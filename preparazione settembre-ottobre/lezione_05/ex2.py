'''Utilizzare una list comprehension per convertire tutte le stringhe di una lista in maiuscolo.'''

string_list: list[str] = ["rosso", "verde", "blu"]

mylist: list[str] = [i.upper() for i in string_list]

print(mylist)


