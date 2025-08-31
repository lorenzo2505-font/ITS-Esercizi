def actions(tris: list[list[str]]) -> list[tuple[int]]: # funzione actions che dato lo stato della griglia, ritorna una lista di tuple contenenti tutte le mosse possibili

    actions_list: list[tuple[int]] = [] # inzializzo una lista di tuple vuota
    
    for el in range(len(tris)): # doppio ciclo
            
        for j in range(len(tris[el])):
                
            if tris[el][j] == "":
                actions_list.append((el, j)) # se la casella è vuta aggiungo una tupla contente l'indice della riga e l'indice della colonna
    
    return actions_list # ritorno la lista di tuple



                    
             

if __name__ == "__main__": # codice driver

    tris1: list[list[str]] = [["", "x", "o"],
                              ["x", "x", "o"],
                              ["", "x", ""]]
    
    print(actions(tris1))
    

    

