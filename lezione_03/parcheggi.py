'''Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli 
da un parcheggio con un numero massimo di posti dato in input.
 L'utente può inserire una delle seguenti opzioni
   "ingresso", "uscita", "stato", "esci". Per ogni opzione:

se l'utente inserisce "ingresso", verifica se ci sono posti disponibili,
 quindi incrementa il numero di posti occupati;
se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, 
quindi decrementa il numero di posti occupati;
se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
se l'utente inserisce "esci", termina l'algoritmo.'''

posti = int(input("inserisci il numero massimo di posti: "))
occupati = 0
option: str = None


while option != "esci":
    option = str(input("inserisci opzione: "))
    if (option != "ingresso") and (option != "uscita") and (option != "stato") and (option != "esci"):
       print("errore")
    else:
        if option == "ingresso":
         if occupati < posti:
                occupati+=1
                posti-=1
         else:
             print("non ci  sono posti disponibili")
         
                
    if option == "uscita":
        if occupati > 0:
                posti+=1
                occupati-=1
        else:
            print("è già tutto libero")
    if option == "stato":
        print(f"i posti occupati sono: {occupati}, mentre quelli liberi sono: {posti}  ")



    
      
    

