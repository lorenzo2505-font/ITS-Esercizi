'''5-11. Numeri ordinali: i numeri ordinali indicano la loro posizione in un elenco, come 1° o 2°.
 La maggior parte dei numeri ordinali termina con th, tranne 1, 2 e 3.
• Memorizzare i numeri da 1 a 9 in un elenco.
• Scorrere l'elenco.
• Utilizzare una catena if-elif-else all'interno del ciclo per stampare la desinenza ordinale corretta per ogni numero. 
Il tuo output dovrebbe essere "1° 2° 3° 4° 5° 6° 7° 8° 9°" e ogni risultato dovrebbe essere su una riga separata.'''

mylist: list[int] =  [1, 2, 3, 4,  5, 6, 7, 8, 9]

for i in mylist:
    if i == 1:
        print("1st!")
    elif i == 2:
        print("2nd!")
    elif i == 3:
        print("3nd!")
    else:
        print(f"{i}th!")
    