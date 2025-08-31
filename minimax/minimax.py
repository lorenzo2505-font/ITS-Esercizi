from terminal import terminal
from value import value
from player import player
import math
from actions import actions
from result import result

def minimax(tris: list[list[str]]) -> int: # funzione per implementare l'algoritmo di minimax, importo tutte le funzioni fatte in precedenza daato che verranno utilizzate tutte

    p = player(tris)
    t = terminal(tris)

    if t: # se il gioco è in stato terminale viene subito ritornato il valore
        
        return value(tris)
    
    if p == "max": # se è il turno di max, il valore deve essere il più alto possibile, si verificheranno tutte le possibili azioni che possiamo fare e capire quale porterà al valore maggiore anche se il giocatore min sta giocando in modo ottimale
        v = -math.inf # così qualsiasi azione che si troverà porterà a un valore maggiore
        a = actions(tris) 

        for action in a: # si ciclano tutte le azioni possibili, per ogni azione che si può intraprendere, si capirà qual è lo stato del gioco risultante e poi si calcolerà il minimax di quel nuovo stato di gioco
            v = max(v, minimax(result(tris, action))) # se è maggiore del miglior valore  trovato finora, v diventa il nuovo valore
        
        return v
    
    elif p == "min": # ora si considera la stessa situazione se è il turno del giocatore min, l'approccio è lo stesso ma si vuole che la variabile sia la più piccola possibile
        v = math.inf # si imposta la variabile al valore più alto possibile, cosìcché ogni azione individuata porterà ad un valore inferiore 
        a = actions(tris)

        for action in a: # si cicla su tutte le azioni possibili
            v = min(v, minimax(result(tris, action)))
        
        return v # si ritorna il valore di v


if __name__ == "__main__": # codice driver
    
    tris1: list[list[str]] = [["", "", ""],
                               ["", "", ""], 
                               ["", "", ""]] # inizializzo una griglia vuota
    
    while not terminal(tris1): # ciclo che termina quando si raggiungerà uno stato terminale
        p = player(tris1) # controllo chi deve giocare con player()

        if p == "max": # se è il turno di max (utente)
            row: int = int(input("inserisci la coordinata della riga: ")) # chiedo all'utente di inserire in input la coordinata della riga
            col: int = int(input("inserisci la coordinata della colonna: ")) # chiedo all'utente di inserire in input la coordinata della colonna
            a = actions(tris1) # variabile contente tutte le azioni possibili

            if (row, col) in a: # se le coordinate sono nell'elenco di a allora il codice può continuare

                tris1 = result(tris1, (row, col)) # aggiorno la griglia specificando le coordinate su cui inserire la croce con la funzione result()
                
            
            else:  # se le coordinate non sono nell'elenco il programma va in errore
                raise ValueError(f"la seguente coppia di coordinate: {(row, col)} non rientra tra le mosse possibili")
        
        elif p == "min": # se è il turno di min (computer)
            a = actions(tris1) # variabile contenente tutte le azioni possibili con actions()
            better_move = ()
            better_point = math.inf

            for el in a: # itero tutte le mosse possibili e per ciascuno calcolo minimax
                m = minimax(result(tris1, el))

                if m < better_point: # condizionale per stabilire un valore minimo
                    better_point = m
                    better_move = el # la tupla conterrà le coordinate dell'azione el
            
            tris1 = result(tris1, better_move) # aggiorno la griglia mettendo le coordinate dell'azione el dove vi è il minimax con il valore più basso

            for i in tris1: # stampo la griglia, riga per riga
                print(i, end="\n")
    
    v = value(tris1) # alla fine del ciclio determino il valore della partita 

    if v == 1: # in base al valore di v determino un vincitore 
        print(f"punteggio: {v}, VINCE L'UTENTE")
    
    if v == 0:
        print(f"punteggio: {v}, PAREGGIO")
    
    if v == -1:
        print(f"punteggio: {v}, VINCE IL COMPUTER")


                
                
            
        
        











    

