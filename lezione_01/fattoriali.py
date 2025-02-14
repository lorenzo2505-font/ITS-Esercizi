n = int(input("inserisci numero: "))
i=1
f=1
if n <= 0:
    print("errore")
else:
    while i <= n:
        f = f * i
        i+=1
print(f)
