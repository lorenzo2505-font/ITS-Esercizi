'''4-10. Slice: utilizzando uno dei programmi che hai scritto in questo capitolo, aggiungi diverse righe alla fine del programma che eseguono le seguenti 
operazioni:
• Stampa il messaggio I primi tre elementi dell'elenco sono:. Quindi usa una sezione per stampare i primi tre elementi dall'elenco di quel programma.
• Stampa il messaggio Tre elementi dal centro dell'elenco sono:. Quindi utilizzare una sezione per stampare tre elementi dal centro dell'elenco.
• Stampa il messaggio Gli ultimi tre elementi dell'elenco sono:. Quindi utilizzare una sezione per stampare gli ultimi tre elementi dell'elenco.'''

cubes: list[int] = []
for i in range(1, 10+1):
    i = i**3
    cubes.append(i)
print(cubes)

print(f"i primi tre elementi dell'elenco sono {cubes[0:3]}")
print(f"i tre elementi del centro sono {cubes[3:6]}")
print(f"gli ultimi elementi sono {cubes[6:10]}")
