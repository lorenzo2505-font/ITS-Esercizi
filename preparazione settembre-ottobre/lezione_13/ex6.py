'''
Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

Calcolare il valore della produttoria Pi se n = 7.'''


def Pi(n: int):

    if n < 0:

        raise ValueError("il numero non può essere negativo")
    
    elif n == 0:

        return (n + 2)
    
    else:

        return (n + 2) * (Pi(n - 1)) 


print(Pi(7))

# 5 / 5


    
    
    