'''Progettare un algoritmo che chieda all'utente di inserire un valore x positivo.
 Se x è negativo, l'algoritmo mostra un messaggio di errore e termina. 
 Se x  è positivo, il programma deve consentire all'utente di inserire 10 numeri sia positivi che negativi. 

    Se x è pari, allora dei numeri inseriti devono essere sommati solamente i numeri che sono maggiori della metà di x. 
    Se, invece, x è dispari, dei numeri inseriti devono essere sommati solo i numeri che sono minori di x. 
'''
x = int(input("inserisci il valore di x: "))
i = 1
somma = 0
if x < 0:
    print("errore")
else:
    while i <= 10:
        n = int(input("inserisci numero: "))
        i+=1
        if (x % 2 == 0) and (n > (x / 2)):
            somma = somma + n
        if (x % 2 != 0) and (n < x):
            somma = somma + n
    print(somma)
        
