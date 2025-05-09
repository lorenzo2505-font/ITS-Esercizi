n = int(input("inserisci numero: "))
i = 0
divisori = 0
if n < 2: 
    print("il numero non è primo")
else:
    while i <= n:
        i+=1
        if n % i == 0:
            divisori+=1
        if divisori >= 2:
            print("il numero non è primo")
            break
        
if divisori < 2:       
    print("il numero è primo")
    

    