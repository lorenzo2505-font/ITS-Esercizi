i = 1
pari = 0
dispari = 0
while i <= 10:
    n = int(input("inserisci numero: "))
    i+=1
    if n % 2 == 0:
        pari+=1
    else:
        dispari+=1
print(pari)
print(dispari)

