'''Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵.
 Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare.
   Se i valori sono validi, calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.'''
a = int(input("inserisci a: "))
b= int(input("inserisci b: "))
i = a
somma = 0
if a >= b:
    print("errore")
else:
    while i <= b:
        somma = somma + i
        i+=1
print(somma)

