'''Creare una list comprehension che include solo le stringhe di lunghezza superiore a 5 caratteri da una lista.'''

lp_songs: list[str] = ["numb", "in the end", "what i've done", "faint", "one step closer"]

mylist: list[str] = [i for i in lp_songs if len(i) > 5]

print(mylist)
