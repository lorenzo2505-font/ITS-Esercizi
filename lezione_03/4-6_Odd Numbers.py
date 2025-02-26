'''Utilizza il terzo argomento della funzione range() per creare un elenco dei numeri dispari da 1 a 20.
 Utilizza un ciclo for per stampare ciascun numero'''

odd: list[int] = []

for i in range (1, 20 +1, 2):
    
    odd.append(i)


print(odd)
