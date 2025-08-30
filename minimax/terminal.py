def terminal(tris: list[list[str]]) -> bool:
    
    counter = 0
    
    if len(tris) != 3:
        
        raise ValueError(f"la lista deve deve contenere non più o meno di 3 elementi")
    
    possible_elements: list[str] = ["x", "o", ""]
    
    for el in range(len(tris)):
        
        if len(tris[el]) != 3:

            raise ValueError("ogni elemento deve contenere a sua volta non più o meno di 3 elementi")
        
        for j in tris[el]:

            if j not in possible_elements:
                
                raise ValueError(f"possono essere inseriti solo i seguenti valori: {possible_elements}")
    
    for i in range(2 + 1):

        if ("x" in tris[i]) and ("o" not in tris[i]) and ("" not in tris[i]):

            return True

        if ("o" in tris[i]) and ("x" not in tris[i]) and ("" not in tris[i]):

            return True
        
        if "" not in tris[i]:
            counter += 1
    
    if (tris[0][0] == "x" and tris[1][0] == "x" and tris[2][0] == "x") or (tris[0][1] == "x" and tris[1][1] == "x" and tris[2][1] == "x") or (tris[0][2] == "x" and tris[1][2] == "x" and tris[2][2] == "x"):

        return True
    
    if (tris[0][0] == "o" and tris[1][0] == "o" and tris[2][0] == "o") or (tris[0][1] == "o" and tris[1][1] == "o" and tris[2][1] == "o") or (tris[0][2] == "o" and tris[1][2] == "o" and tris[2][2] == "o"):

        return True
    
    if (tris[0][0] == "x" and tris[1][1] == "x" and tris[2][2] == "x") or (tris[0][2] == "x" and tris[1][1] == "x" and tris[2][0] == "x"):

        return True
    
    if (tris[0][0] == "o" and tris[1][1] == "o" and tris[2][2] == "o") or (tris[0][2] == "o" and tris[1][1] == "o" and tris[2][0] == "o"):

        return True
    
    if counter == 3:

        return True
    
    return False
    
    
    
    
if __name__ == "__main__":



    tris1: list[list[str]] = [["", "x", "o"],
                            ["x", "o", ""],
                            ["x", "", "x"]]

    tris2: list[list[str]] = [["x", "x", "o"],
                            ["x", "o", "o"],
                            ["x", "", ""]] 

    print(terminal(tris1))
    print(terminal(tris2))
            
        
     
        
        
        
        
    