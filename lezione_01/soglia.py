soglia = int(input("inserisci soglia: "))
i = 1
cont_soglia = 0
while i <= 7:
    n = int(input("inserisci numero: "))
    i+=1
    if n > soglia:
        cont_soglia+=1
print(f"ci sono {cont_soglia} numeri che superano la soglia")
