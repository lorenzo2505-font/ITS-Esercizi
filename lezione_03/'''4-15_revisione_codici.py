'''4-15. Revisione del codice: scegli tre dei programmi che hai scritto in questo capitolo e modifica ciascuno di essi per conformarsi al PEP 8.'''

#my pizzas your pizzas

pizzas: list [str] = [
    "Margherita","Patate","Diavola"
    ] #definisco la lista delle mie pizze


pizzas.append("Rossa") #aggiungo la pizza rossa alla mia lista di pizze


friend_pizzas: list [str] = [
    "Margherita","Patate","Diavola"
    ] #definisco la lista delle pizze dell'amico

friend_pizzas.append("Patate E Salsicce") #aggiungo la pizza patate e salsicee alla lista pizze dell'amico

for i in range(0, len(pizzas)):
    print(f"le mie pizze preferite: {pizzas[i]}") #faccio in ciclo for e chiedo di stampare l'elenco delle mie pizze per ogni elemento da 0 fino alla lunghezza della lista


for i in range(0, len(friend_pizzas)):
    print(f"le pizze preferite del mio amico: {friend_pizzas[i]}") #faccio un ciclo for e chiedo di stampare l'elenco delle pizze del mio amico per ogni elemento da 0 fino alla lunghezza della lista

#odd numbers 

odd: list[int] = [] #definisco una lista inizialmente vuota

for i in range (1, 20 +1, 2):
    
    odd.append(i) #faccio un ciclo for in cui per ogni elemento da 1 a 20 saltando di 2 lo aggiungo alla lista


print(odd) #stampo la lista 


#threes 

mylist: list[int] = [] #definisco una lista inzialmente vuota


for i in range(3, 30 +1):
    if i % 3 == 0:
        mylist.append(i) #faccio un ciclo for con if in cui per ogni elemnto da 3 a 30 se è divisibile per 3 lo aggiungo alla lista 


print(mylist) #stampo la lista
