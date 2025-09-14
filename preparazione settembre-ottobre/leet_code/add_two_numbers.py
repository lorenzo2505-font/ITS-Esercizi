'''Ti vengono fornite due liste concatenate non vuote che rappresentano due numeri interi non negativi.
Le cifre sono memorizzate in ordine inverso e ciascuno dei loro nodi contiene una singola cifra.
Somma i due numeri e restituisci la somma come lista concatenata.

Puoi supporre che i due numeri non contengano nessuno zero iniziale, ad eccezione del numero 0 stesso.'''

def addTwoNumbers(l1: list[int], l2: list[int]):

    l3: list[int] = []

    for i in l1:

        if i <= 0:
            raise ValueError("no negative numbers here")
    
    for i in l2:

        if i <= 0:
            raise ValueError("no negative numbers here")
    
    number1: str = ""
    number2: str = ""

    for i in l1[::-1]:
        number1 += str(i)
    
    for i in l2[::-1]:
        number2 += str(i)
    
    somma: int = int(number1) + int(number2)
    
    for i in str(somma)[::-1]:
        l3.append(int(i))
    
    return l3

    


print(addTwoNumbers([2,4,3], [5,6,4]))







        