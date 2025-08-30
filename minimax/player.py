def player(tris: list[list[str]]) -> str:

    count_x = 0
    count_o = 0
    
    if len(tris) != 3:
        
        raise ValueError(f"la lista deve deve contenere non più o meno di 3 elementi")
    
    possible_elements: list[str] = ["x", "o", ""]
    
    for el in range(len(tris)):
        
        if len(tris[el]) != 3:

            raise ValueError("ogni elemento deve contenere a sua volta non più o meno di 3 elementi")
        
        for j in tris[el]:

            if j not in possible_elements:
                
                raise ValueError(f"possono essere inseriti solo i seguenti valori: {possible_elements}")
            
            if j == "x":
                count_x += 1
            
            elif j == "o":
                count_o += 1
        
    if (count_x == 0 and count_o == 0) or (count_x == count_o):

        return "max"
        
    if count_x > count_o:
            
        return "min"
        
    if count_o > count_x:

        raise ValueError("le o non possono essere maggiori delle x")


if __name__ == "__main__":

    tris1: list[list[str]] = [["", "", "o"],
                              ["", "x", ""],
                              ["", "", ""]]

    tris2: list[list[str]] = [["", "x", ""],
                              ["x", "o", ""],
                              ["", "", ""]]

    print(player(tris1)) 
    print(player(tris2))




    
    
