'''Dato un intero a 32 bit con segno x, restituisci x con le cifre invertite.
Se l'inversione di x causa un'uscita del valore dall'intervallo degli interi a 32 bit con segno [-2^31, 2^31 - 1], restituisci 0.'''

def reverse_integer(x: int) -> int:
    
    newint = str(x).strip("-0")
    
    if x < 0:

        if -int(newint[::-1]) not in range(-2**31, 2**31):
            
            return 0
    
        return -int(newint[::-1])
    
    else:
        
        if int(newint[::-1]) not in range(-2**31, 2**31):
            
            return 0
        
        return int(newint[::-1])

def main():

    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(102))
    print(reverse_integer(-1020))
    

main()
    