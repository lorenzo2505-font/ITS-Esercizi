def player(tris: list[list[str]]) -> str:

    count_x = 0 
    count_o = 0 # vengono inizializzati dei contatori vuoti
    
    if len(tris) != 3: # controlli per verificare che la griglia sia 3 X 3 e che contenga solo i caratteri relativi alle croci, cerchi o caselle vuote
        
        raise ValueError(f"la lista deve deve contenere non più o meno di 3 elementi")
    
    possible_elements: list[str] = ["x", "o", ""]
    
    for el in range(len(tris)):
        
        if len(tris[el]) != 3:

            raise ValueError("ogni elemento deve contenere a sua volta non più o meno di 3 elementi")
        
        for j in tris[el]:

            if j not in possible_elements:
                
                raise ValueError(f"possono essere inseriti solo i seguenti valori: {possible_elements}")
            
            if j == "x":
                count_x += 1 # sommo il numero di "x" con il contatore
            
            elif j == "o":
                count_o += 1 # sommo il numero di "o" con il contatore 
        
    if (count_x == 0 and count_o == 0) or (count_x == count_o): # se nessuno ha ancora giocato o i due contatori sono uguali è il turno di max("x")

        return "max"
        
    if count_x > count_o: # se ci sono più "x" che "o" tocca min ("o")
            
        return "min"
        
    if count_o > count_x: # se ci sono più cerchi che croci mando il programma in errore

        raise ValueError("le o non possono essere maggiori delle x")


if __name__ == "__main__": # codice driver

    tris1: list[list[str]] = [["", "", "o"],
                              ["", "x", ""],
                              ["", "", ""]]

    tris2: list[list[str]] = [["", "x", ""],
                              ["x", "o", ""],
                              ["", "", ""]]

    print(player(tris1)) 
    print(player(tris2))




    
    
