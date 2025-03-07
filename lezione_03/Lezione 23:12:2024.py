#while
lista1 :list=[1, 2, 3, 4, 5]
contatore: int=0
while contatore < len(lista1):
    print(lista1[contatore])
    contatore+=1


#for

for lettera in lista1:
    print(lettera)


#esempio while

Utenti_E_Password: dict={"flavio": "1234", "giovanni": "5678", "marco":  "91011" }
nome_utente=  str(input("inserisci il nome utente"))
Password =  Utenti_E_Password[nome_utente]
while True:  #ciclo infinito 
    b= input("inserisci la  password")
    if b==Password:
        print("password corretta")
        break  #rompe il ciclo
    else: 
        print("password errata")
        pass #il programma tiene questa istruzione in considerazione ma di  base non fa nulla







#break and continue 
for i in range(10):
    if i==5:
        continue #salta il 5 in  output 
    print(i)



