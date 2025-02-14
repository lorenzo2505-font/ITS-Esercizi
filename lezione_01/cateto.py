import math 
a = float(input("inserisci il valore dell'ipotenusa: "))
b= float(input("inserisci il valore del cateto: "))
if a > b:
    c = math.sqrt(a**2 - b**2)
    print(f"l'altro cateto vale: {c}")
else:
    print("errore")
