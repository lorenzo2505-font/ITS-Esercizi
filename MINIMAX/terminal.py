def terminal(tris: list[list[str]]) -> bool: # funzione per capire se il gioco è in una fase terminale 
    
    counter = 0
    
    if len(tris) != 3: # controlli per verificare che la griglia sia 3 X 3 e che i simboli siano solo "x"(croce), "o" (cerchio), "" (casella vuota)
        
        raise ValueError(f"la lista deve deve contenere non più o meno di 3 elementi")
    
    possible_elements: list[str] = ["x", "o", ""]
    
    for el in range(len(tris)):
        
        if len(tris[el]) != 3:

            raise ValueError("ogni elemento deve contenere a sua volta non più o meno di 3 elementi")
        
        for j in tris[el]:

            if j not in possible_elements:
                
                raise ValueError(f"possono essere inseriti solo i seguenti valori: {possible_elements}")
    
    for i in range(2 + 1): # controllo le condizioni di vittoria sulle righe sia per "x" che per "o" (utilizzando gli indici)

        if ("x" in tris[i]) and ("o" not in tris[i]) and ("" not in tris[i]):

            return True

        if ("o" in tris[i]) and ("x" not in tris[i]) and ("" not in tris[i]):

            return True
        
        if "" not in tris[i]: # controllo se tutte le caselle di ogni riga sono occupate, se lo sono incremento il valore di un contatore inizializzato a 0
            counter += 1 
    
    if (tris[0][0] == "x" and tris[1][0] == "x" and tris[2][0] == "x") or (tris[0][1] == "x" and tris[1][1] == "x" and tris[2][1] == "x") or (tris[0][2] == "x" and tris[1][2] == "x" and tris[2][2] == "x"): # controllo vittoria sulle colonne per "x" (utilizzando gli indici)

        return True
    
    if (tris[0][0] == "o" and tris[1][0] == "o" and tris[2][0] == "o") or (tris[0][1] == "o" and tris[1][1] == "o" and tris[2][1] == "o") or (tris[0][2] == "o" and tris[1][2] == "o" and tris[2][2] == "o"): # controllo vittoria sulle colonne per "o" (utilizzando gli indici)

        return True
    
    if (tris[0][0] == "x" and tris[1][1] == "x" and tris[2][2] == "x") or (tris[0][2] == "x" and tris[1][1] == "x" and tris[2][0] == "x"): # controllo vittoria sulle diagonali per "x" (utilizzando gli indici)

        return True
    
    if (tris[0][0] == "o" and tris[1][1] == "o" and tris[2][2] == "o") or (tris[0][2] == "o" and tris[1][1] == "o" and tris[2][0] == "o"): # controllo vittoria sulle diagonali per "o" (utilizzando gli indici)

        return True
    
    if counter == 3: # controllo pareggio, con il contatore rilevo se tutte le righe sono piene senza vincitori

        return True
    
    return False # se nessuna delle precedenti condizioni si è verificata allora ritorno False
    
    
    
    
if __name__ == "__main__": # codice driver



    tris1: list[list[str]] = [["", "x", "o"],
                            ["x", "o", ""],
                            ["x", "", "x"]]

    tris2: list[list[str]] = [["x", "x", "o"],
                            ["x", "o", "o"],
                            ["x", "", ""]] 

    print(terminal(tris1))
    print(terminal(tris2))
            
        
     
        
        
        
        
    