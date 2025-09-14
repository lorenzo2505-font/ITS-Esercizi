'''Esercizio 3 - Uso con filter()
Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. Usa filter() con una lambda per ottenere solo i numeri pari.'''

numeri: list[int] = [5, 12, 17, 18, 24, 32]

pari = list(filter(lambda n : n % 2 == 0, numeri))

print(pari)



