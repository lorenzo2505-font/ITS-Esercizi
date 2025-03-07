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