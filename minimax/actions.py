def actions(tris: list[list[str]]) -> list:

    actions_list: list[tuple] = []
    
    for el in range(len(tris)):
            
        for j in range(len(tris[el])):
                
            if tris[el][j] == "":
                actions_list.append((el, j))
    
    return actions_list



                    
             

if __name__ == "__main__":

    tris1: list[list[str]] = [["", "x", "o"],
                              ["x", "x", "o"],
                              ["", "x", ""]]
    
    print(actions(tris1))
    

    

