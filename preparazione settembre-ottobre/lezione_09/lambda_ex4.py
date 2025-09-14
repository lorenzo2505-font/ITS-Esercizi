'''Esercizio 4 - Ordinamento con sorted()
Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)].
Ordina la lista in base all'età (secondo elemento) usando sorted() e lambda.'''


studenti: list[tuple] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

s_age: list = sorted(studenti, key = lambda age: age[1])

print(s_age)

