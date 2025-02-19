'''Vedere il mondo: pensa ad almeno cinque posti nel mondo che ti piacerebbe visitare.
• Memorizzare le posizioni in un elenco. Assicurati che l'elenco non sia in ordine alfabetico.
• Stampa l'elenco nell'ordine originale. Non preoccuparti di stampare l'elenco in modo ordinato; basta stamparlo come un elenco Python grezzo.
• Utilizzare sorted() per stampare l'elenco in ordine alfabetico senza modificare l'elenco reale.
• Mostra che l'elenco è ancora nell'ordine originale stampandolo.
• Utilizzare sorted() per stampare l'elenco in ordine alfabetico inverso senza modificare l'ordine dell'elenco originale.
• Mostra che l'elenco è ancora nell'ordine originale stampandolo di nuovo.
• Usa reverse() per cambiare l'ordine della tua lista. Stampa l'elenco per mostrare che il suo ordine è cambiato.
• Usa reverse() per cambiare nuovamente l'ordine della tua lista. Stampa l'elenco per mostrare che è tornato al suo ordine originale.
• Utilizza sort() per modificare l'elenco in modo che sia memorizzato in ordine alfabetico. 
Stampa l'elenco per mostrare che il suo ordine è stato modificato.
• Utilizza sort() per modificare l'elenco in modo che venga memorizzato in ordine alfabetico inverso.
Stampa l'elenco per mostrare che il suo ordine è cambiato.'''

world: list = ["Londra", "Madrid", "Tokyo", "Barcellona", "New York"]

print(world)
print(sorted(world))
print(world)
print(sorted(world, reverse = True))
print(world)

'''world=sorted(world)
world.reverse()   
print(world)''' #come usare sorted e reverse per modificare la lista

world.reverse()
print(world)

world.reverse()
print(world)

world.sort()
print(world)


world.sort()
world.reverse()
print(world)

