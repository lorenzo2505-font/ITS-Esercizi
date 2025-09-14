quadrati = [n**2 for n in range(10)]

print(quadrati)


lista1 = [1, 2, 3]
lista2 = [3, 1, 4]

mix = [(x, y) for x in lista1 for y in lista2 if x != y] # con le lista compressa

'''for x in lista1: # metodo base
    for y in lista2:
        if x != y:
            mix.append((x, y))'''

print(mix)

stringati = [str(n) for n in lista1]

print(stringati)