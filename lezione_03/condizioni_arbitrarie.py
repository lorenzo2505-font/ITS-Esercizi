'''13. Esercizio di controllo numerico con condizioni arbitrarie

Progettare un algoritmo che verifichi se tre numeri interi positivi x, y, z rispettano le seguenti regole:

la somma di x+y+z deve essere pari;
x deve essere divisibile per 3, y divisibile per 5 e z divisibile per 7;
se entrambe le condizioni sono vere, mostrare: “Regole rispettate”. Altrimenti, mostrare:
 “Regole non rispettate”.'''

x = int(input("inserisci x: "))
y = int(input("inserisci y: "))
z = int(input("inserisci z: "))

if (x < 0) and (y < 0) and (z < 0):
    print("errore")
else:
    if ((x + y + z) % 2 == 0) and (x %  3 == 0) and (y % 5 == 0) and (z % 7 == 0):
        print("regole rispettate")
    else:
        print("regole non rispettate")
        