'''Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario.
 Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
 Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"'''

'''persona: dict = { "nome":
    {"ruolo":
     "età"
     

    }
}'''

persona: dict = {"nome": "", "ruolo": "", "età": ""}

nome = str(input("inserisci nome: "))
persona["nome"] = nome

ruolo = str(input("inserisci ruolo: "))
persona["ruolo"] = ruolo

età = int(input("inserisci età: "))
persona["età"] = età



match persona:
    case persona if persona["ruolo"] == "admin":
        print(f"hai accesso a tutte le funzionalità, {nome}")
    case persona if persona["ruolo"] == "moderatore":
        print(f"puoi gestire tutti i contenuti ma non puoi modificare le impostazioni, {nome}")
    case persona if persona["età"] >= 18 and persona["ruolo"] == "utente":
        print(f"sei un utente che ha accesso standard a tutti i servizi, {nome}")
    case persona if persona["età"] < 18 and persona["ruolo"] == "utente":
        print(f"sei un utente che ha accesso limitato e alcune funzionalità sono limitate, {nome}")
    case persona if persona["ruolo"] == "ospite":
        print(f"accesso ristretto, puoi solo visualizzare i contenuti, {nome}")
    case _  :
        print("ruolo non riconosciuto")


'''match persona: ####
        
'''

# test b
        

    
    
    

