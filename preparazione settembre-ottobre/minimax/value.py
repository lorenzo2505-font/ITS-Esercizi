from terminal import terminal


def value(tris: list[list[str]]) -> int: # funzione che dato lo stato di una griglia fornisce un valore 

    t = terminal(tris) # il punteggio verrà stabilito solo se il gioco è finito, viene quindi importata la funzione terminal

    if t:
        counter = 0

        for i in range(2 + 1): # come nella funzione terminal controllo tutte le possibilità di vittoria per "x" oppure "o" su righe, colonne e diagonali utilizzando gli indici, ritorno 1 per "x", -1 per "o"

            if ("x" in tris[i]) and ("o" not in tris[i]) and ("" not in tris[i]):

                return 1

            if ("o" in tris[i]) and ("x" not in tris[i]) and ("" not in tris[i]):

                return -1
        
            if "" not in tris[i]:
                counter += 1
        
        if (tris[0][0] == "x" and tris[1][0] == "x" and tris[2][0] == "x") or (tris[0][1] == "x" and tris[1][1] == "x" and tris[2][1] == "x") or (tris[0][2] == "x" and tris[1][2] == "x" and tris[2][2] == "x"):

            return 1
        
        if (tris[0][0] == "o" and tris[1][0] == "o" and tris[2][0] == "o") or (tris[0][1] == "o" and tris[1][1] == "o" and tris[2][1] == "o") or (tris[0][2] == "o" and tris[1][2] == "o" and tris[2][2] == "o"):

            return -1
        
        if (tris[0][0] == "x" and tris[1][1] == "x" and tris[2][2] == "x") or (tris[0][2] == "x" and tris[1][1] == "x" and tris[2][0] == "x"):

            return 1
        
        if (tris[0][0] == "o" and tris[1][1] == "o" and tris[2][2] == "o") or (tris[0][2] == "o" and tris[1][1] == "o" and tris[2][0] == "o"):

            return -1
        
        if counter == 3: # come nella funzione terminal, controllo la possibilità di pareggio e nel caso ritorno 0

            return 0
    
    return None


if __name__ == "__main__": # codice driver

    tris1: list[list[str]] = [["x", "x", "o"],
                              ["x", "o", "o"],
                              ["x", "", ""]]
    
    tris2: list[list[str]] = [["", "x", "o"],
                              ["x", "o", "x"],
                              ["o", "", ""]]
    
    print(value(tris1))
    print(value(tris2))


        

        
        