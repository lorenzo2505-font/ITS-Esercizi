from player import player 

def result(tris: list[list[str]], action: tuple[int]) -> list[list[str]]:

    if len(action) != 2: # controllo che la tupla contenente la mossa abbia solo due elementi (l'indice della riga e della colonna)

        raise ValueError("la tupla non può avere più o meno di due elementi")
    
    if action[0] not in range(0, 2 + 1) or action[1] not in range(0, 2 + 1): # controllo che gli indici siano in un intervallo [0:2]

        raise IndexError("uno degli indici della tupla non è compreso nell'intervallo di valori [0:2]")
    
    if tris[action[0]][action[1]] != "": # controllo che la casella sia vuota prima di inserire la croce o il cerchio

        raise ValueError("questa casella è già occupata")
    
    p = player(tris) # importo la funzione player per verificare di chi è il turno
    newlist: list[list[str]] = [i.copy() for i in tris] # creo una copia della griglia 

    if p == "max": # se è il turno di max la casella verrà riempita con una crocetta grazie alle coordinate fornite dalla tupla e utilizzando gli indici
        newlist[action[0]][action[1]] = "x"
    
    else: # se è il turno di min la casella verrà riempita con un cerchio grazie alle coordinate fornite dalla tupla e utilizzando gli indici
        newlist[action[0]][action[1]] = "o"

    return newlist # restituisco la nuova lista con la casella riempita

if __name__ == "__main__": # codice driver

    tris1: list[list[int]] = [["", "x", "o"],
                              ["x", "x", "o"],
                              ["", "o", ""]]
    
    mossa: tuple[int] = (2, 2)

    print(result(tris1, mossa))
    
    