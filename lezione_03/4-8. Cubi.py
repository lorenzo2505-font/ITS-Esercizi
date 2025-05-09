'''4-8. Cubi: Un numero elevato alla terza potenza si chiama cubo. Ad esempio, il cubo di 2 è scritto come 2**3 in Python.
 Crea un elenco dei primi 10 cubi (ovvero il cubo di ciascun numero intero da 1 a 10) e utilizza un ciclo for per stampare il valore di ciascun cubo.'''

cubes: list[int] = []
for i in range(1, 10+1):
    i = i**3
    cubes.append(i)
print(cubes)