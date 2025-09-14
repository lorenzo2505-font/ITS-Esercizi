'''Creare una list comprehension che estrae le vocali da una stringa data.'''

mystr: str = "crawling"

mylist: list[str] = [i for i in mystr if i == "a" or i == "e" or i == "i" or i == "o" or i == "u"]

print(mylist)