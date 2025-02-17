'''14. Simulazione di un gioco di dadi

Progettare un algoritmo che simuli un gioco basato sul lancio di due dadi virtuali a sei facce, D1 e D2. 
L'algoritmo deve eseguire le seguenti operazioni:

Simulare il lancio dei due dadi.
Calcolare la somma dei valori ottenuti dai due dadi.
Applicare le seguenti regole di gioco per determinare il punteggio:
Se entrambi i dadi mostrano numeri pari e la somma è maggiore di 8, il giocatore vince e il punteggio è
 impostato direttamente a 100.
Se uno dei dadi mostra 6 oppure la somma è uguale a 7, il punteggio del giocatore viene incrementato di 10.
In tutti gli altri casi, il giocatore perde e il punteggio è impostato a 0.
Mostrare il risultato del gioco e il punteggio ottenuto.
Il gioco continua finché il punteggio totale del giocatore non raggiunge 100 (vittoria) 
oppure scende a zero (sconfitta).'''

while True:
    punteggio: int
    D1 = int(input("lancio del primo dado: "))
    D2 = int(input("lancio del secondo dado: "))
    somma = D1 + D2
    if (D1 > 6) and (D2 > 6) and (D1 <= 0) and (D2 <= 0):
      print("errore")
    else:
        if (D1 % 2 == 0) and (D2 % 2 == 0) and (somma > 8):
          punteggio = 100
          print(f"il giocatore ha vinto, il punteggio è {punteggio}")
          break
        if (D1 == 6) or (D2 == 6) or (somma == 7):
           punteggio = somma + 10
           print(f"il punteggio è {punteggio}")
        
           
           
        else:
           punteggio = 0
           print(f"il giocatore  ha perso, il punteggio è {punteggio}")
           break
    




        

           
          
        
    
          


    
    




