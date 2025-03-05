'''4-1. Pizze: pensa ad almeno tre tipi della tua pizza preferita. Memorizza questi nomi di pizza in un elenco, 
quindi utilizza un ciclo for per stampare il nome di ciascuna pizza.
• Modifica il tuo ciclo for per stampare una frase usando il nome della pizza,
 invece di stampare solo il nome della pizza. Per ogni pizza, 
 dovresti avere una riga di output contenente una semplice affermazione come Mi piace la pizza ai peperoni.
• Aggiungi una riga alla fine del tuo programma, fuori dal ciclo for, che indichi quanto ti piace la pizza.
 L'output dovrebbe essere composto da tre o più righe sui tipi di pizza che ti piacciono e poi da una frase aggiuntiva, 
 ad esempio Adoro davvero la pizza!'''

from typing import Any

ristorante = ["Frontoni", "Sicilia", "Mucca pazza"]
pizzas: list[str] = ["Margherita", "Patate", "Diavola"]
for i in pizzas:
    
    print(f"come mi piace la {i} !")

print("vado pazzo per la pizza !")

'''
for i in range(0, len(pizza)):
    print(f"che buona la {pizza[i]} da {ristorante[i]}")''' #altro metodo
