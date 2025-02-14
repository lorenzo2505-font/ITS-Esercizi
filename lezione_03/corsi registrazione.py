'''Progetta un algoritmo che gestisca l'iscrizione degli studenti a corsi disponibili in una università. 
Per ogni corso ci sono un massimo di 100 posti liberi.
 Richiesto il nome del corso, mostra un menu con le seguenti opzioni "iscrivi", "annulla", "visualizza", "elimina", ed "Esci".

    se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili per il corso, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "annulla", decrementa il numero di posti occupati;
    se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati nel corso;
    se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
    se l'utente inserisce "esci", termina l'algoritmo.
'''

corsi: dict = {
    "Informatica": {
        "posti_liberi" : 100,
        "posti_occupati" : 0

    },
    "Ingegneria Meccanica" : {
        "posti_liberi" : 100,
        "posti_occupati" : 0
    },
    "Economia" : {
        "posti_liberi" : 100,
        "posti_occupati" : 0

    },

    "Medicina" : {
        "posti_liberi" : 100,
        "posti_occupati" : 0
    }
}
option: str = None
nome_corso = None
while True:
    
    option = str(input("inserisci opzione: "))
    if option == "esci":
        break
    nome_corso = input("inserisci corso: ")
    if (option != "iscrivi") and (option != "annulla") and (option != "visualizza") and (option != "elimina") and (option != "esci"):
        print("errore")
    else:
        
        if option == "iscrivi":
            if corsi[nome_corso.title()] ["posti_occupati"] < corsi[nome_corso.title()] ["posti_liberi"] :
                corsi[nome_corso.title()] ["posti_occupati"]+=1
                corsi[nome_corso.title()] ["posti_liberi"]-=1
                
            else:
                print("posti esauriti")
        if option == "annulla":
            if corsi[nome_corso.title()] ["posti_occupati"] > 0:
                corsi[nome_corso.title()] ["posti_liberi"]+=1
                corsi[nome_corso.title()] ["posti_occupati"]-=1
            else:
                print("tutto libero")
        if option == "visualizza":
            posti_occupati = corsi[nome_corso.title()]["posti_occupati"]
            posti_liberi =  corsi[nome_corso.title()]["posti_liberi"]
            print(f"i posti occupati di questo corso sono: {posti_occupati}, mentre i posti liberi sono: {posti_liberi}")
        if option == "elimina":
            del corsi[nome_corso.title()]
            new_corso = input("inserisci nuovo corso: ")
            corsi[new_corso.title()] = {
                    "posti_liberi" : 100,
                    "posti_occupati" : 0

                }
        
            
'''
corsi: dict = { 
    "Informatica": { 
        "Posti_liberi": 100,
        "Posti_occupati: 0,
        "Posti_totali: 100
    },
    "Ingegneria Informatica": { 
        "Posti_liberi": 100,
        "Posti_occupati: 0,
        "Posti_totali: 100
    }
}
nome_corso = None

while True:
    nome_corso = input("Inserisci il nome del corso")



    corsi[nome_corso]["Posti_liberi"] -= 1
    corsi[nome_corso]["Posti_occupati"] += 1

    '''
