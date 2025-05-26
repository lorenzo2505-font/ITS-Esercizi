import random

import time 


def moves_t (t: int):
    probabilità = random.randint(1, 10)
    
    if 1 <= probabilità <= 5: #50% passo veloce
        t += 3
    
    elif 6 <= probabilità <= 7: #20% scivolata
        t -= 6
        if t < 1:
            t = 1
    else: #30% passo lento
       t += 1
    
    return t  



    
    
    
    
   



def moves_h (h: int):
    probabilità = random.randint(1, 10)
    

    if 1<= probabilità <= 2: #20% riposo
        h = h

    elif 3<= probabilità <= 4: #20% passo lento
        h += 9

    elif probabilità == 5:  #10% gran scivolata
        h -= 12
        if h < 1:
            h = 1

    elif 6<= probabilità <= 8: #30% piccolo balzo
        h += 1

    else: #20% piccola scivolata
        h -= 2
        if h < 1:
            h = 1
    return h

def gestione_posizioni(turt_pos, h_pos):
    gara: list = []

    for i in range (1, 70+1):
        i = "_"
        gara.append(i)
    
    
    if turt_pos >= 70 and h_pos >= 70:
        turt_pos = 70
        h_pos= 70
        gara[turt_pos -1] = "Ouch !"
        print(*gara)
        print("\n\n Tie !\n")

    elif turt_pos >= 70:
        turt_pos = 70
        gara[turt_pos - 1] = "T"
        gara[h_pos - 1] = "H"
        print(*gara)
        print("\n\n Turtle Wins !\n")

    elif h_pos >= 70:
        h_pos = 70
        gara[turt_pos - 1] = "T"
        gara[h_pos - 1] = "H"
        print(*gara)
        print("\n\n Hare Wins !\n")

    elif turt_pos == h_pos:
        gara[turt_pos -1] = "Ouch !"
        print(*gara)

    else:
        gara[turt_pos - 1] = "T"
        gara[h_pos - 1] = "H"
        print(*gara)

    


#this is MAIN
turt_pos = 1
h_pos = 1

print("\n BOOM !\n\n")

while True:
    time.sleep(1)
    
    turt_pos = moves_t (turt_pos)
    h_pos = moves_h (h_pos)

    gestione_posizioni (turt_pos, h_pos)

    if turt_pos >= 70 or h_pos >= 70:
        break

#perfect



    


    
    

    
    
    
    



    



    
        
   


