#inserimento del numero 
n = int(input("inserisci  numero: "))

match n:
    #n positivo e pari
    case n if (n > 0) and (n % 2 ==  0):
        print(f"{n} è positivo e pari")
    #n positivo e dispari
    case n if (n > 0) and (n % 2 != 0):
        print(f"{n} è positivo e dispari")
    #n negativo e pari
    case n if  (n <  0) and (n % 2 == 0):
        print(f"{n} è negativo e pari")
    #n negativo e dispari
    case n if (n < 0)  and (n % 2 != 0):
        print(f"{n} è negativo e dispari")
    case _  :
        print("il numero che hai inserito è uguale a 0")
        
