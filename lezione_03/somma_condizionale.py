'''18. Classifica e somma condizionale

Scrivere un algoritmo che consenta all’utente di inserire una numero variabile
 di numeri interi (la quantità è scelta dall’utente). L'algoritmo deve:

sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;
Mostrare in output entrambe le somme e indicare quale somma è maggiore.'''

n = int(input("quanti numeri vuoi inserire ?: "))
i = 1
somma = 0
somma_pari = 0
somma_dispari = 0
while i <= n:
    a = int(input("inserisci numero: "))
    i+=1
    somma = somma + a
    media = somma / i
    if (a % 2 == 0) and (a > media):
        somma_pari = somma_pari + a
    if (a % 2 != 0) or (a < media):
        somma_dispari = somma_dispari + a
print(somma_pari)
print(somma_dispari)
if somma_pari  > somma_dispari:
    print(f"questo tipo di somma: {somma_pari}, è maggiore rispetto a quest'altro: {somma_dispari}")
if somma_dispari > somma_pari:
    print(f"questo tipo di somma: {somma_dispari}, è maggiore rispetto a quest'altro: {somma_pari}")
    



