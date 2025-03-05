'''
4-11. Le mie pizze, le tue pizze: inizia con il programma dell'esercizio 4-1. Crea una copia dell'elenco delle pizze e chiamala friend_pizzas. 
Quindi, procedi come segue:
• Aggiungere una nuova pizza all'elenco originale.
• Aggiungi una pizza diversa alla lista friends_pizzas.
• Dimostra di avere due elenchi separati. Stampa il messaggio Le mie pizze preferite sono:, 
quindi utilizza un ciclo for per stampare il primo elenco.
 Stampa il messaggio Le pizze preferite del mio amico sono:, quindi utilizza un ciclo for per stampare il secondo elenco. 
 Assicurati che ogni nuova pizza sia memorizzata nell'elenco appropriato.'''

pizzas: list[str] = ["Margherita", "Patate", "Diavola"]
pizzas.append("Rossa")
friend_pizzas: list[str] = ["Margherita", "Patate", "Diavola"]
friend_pizzas.append("Patate E Salsicce")
for i in range(0, len(pizzas)):
    print(f"le mie pizze preferite: {pizzas[i]}")
for i in range(0, len(friend_pizzas)):
    print(f"le pizze preferite del mio amico: {friend_pizzas[i]}")