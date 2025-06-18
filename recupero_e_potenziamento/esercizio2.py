def inserisci (n: int):


    if type(n) == int and n > 0:

        return True
    
    else:

        return False



def sequenza(x: int):

    sequenza: list [int] = []

    t = inserisci(x)

    if t == True:

        while True:

            numero: int = int(input("inserisci numero: "))

            if numero <= 0:
                break

            

            sequenza.append(numero)
    
    print(sequenza)

    print(f"il numero {x} appare nella sequenza per {sequenza.count(x)} volte")

    for i in range(len(sequenza)):

        if sequenza[i] == x:

            print(f"il numero {x} appare per la prima volta nella posizione {i}")
            break
    
    somma = 0

    for i in sequenza:

        if i != x:

            somma += i
            
    print(somma)

    

        
    
    




sequenza(3)
        
        
    
    

    


            

