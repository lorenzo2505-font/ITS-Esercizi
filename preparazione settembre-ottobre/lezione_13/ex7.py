'''
Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. 

Sia Pi3 una produttoria definita come segue:
Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  

Calcolare il valore della produttoria Pi3 se n = 5.'''

def Pi3(n: int):

    if n < 0:

        raise ValueError("il numero non può essere negativo")
    
    elif n == 0:

        return 1
    
    else:

        return (n ** 3) * (Pi3(n - 1))


print(Pi3(5))
