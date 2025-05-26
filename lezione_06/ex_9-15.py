'''9-14. Lotteria: crea una classe LotteryMachine che contenga una lista contenente una serie di 10 numeri e 5 lettere.
 Implementa un metodo per selezionare casualmente 4 elementi (numeri o lettere) da questa lista per estrarre un biglietto vincente. 
 Infine, 
 implementa un metodo per visualizzare un messaggio che indichi che qualsiasi biglietto che corrisponda ai 4 elementi vincenti vince un premio.'''


import random

from typing import Any




class LotteryMachine:

    def __init__(self):

        self.mylist: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

    def select(self):

        elementi_selezionati: list = []


        for i in range(1, 4 + 1):


            scelta = random.choice(self.mylist)

            elementi_selezionati.append(scelta)
        
        self.sel = elementi_selezionati
        
        print(elementi_selezionati)
    
    def messaggio(self, biglietto: Any):

        if biglietto not in self.mylist:

            print("errore")
        
        else:

            if biglietto in self.sel:

                print("ha vinto, il biglietto corrisponde a uno dei 4 elementi vincenti")
            
            else:

                print("il biglietto non corrisponde a uno dei nostri 4 elementi vincenti")


l: LotteryMachine = LotteryMachine ()

l.select()

l.messaggio(10)

        

            