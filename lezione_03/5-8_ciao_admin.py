'''5-8. Ciao amministratore: crea un elenco di cinque o più nomi utente, incluso il nome "amministratore". 
Immagina di scrivere un codice che stamperà un saluto a ciascun utente dopo aver effettuato l'accesso a un sito Web. 
Scorri l'elenco e stampa un saluto per ciascun utente.
• Se il nome utente è "admin", stampa un messaggio di saluto speciale, ad esempio Ciao amministratore, desideri visualizzare un rapporto sullo stato?
• Altrimenti, stampa un saluto generico, come Ciao Jaden, grazie per aver effettuato nuovamente l'accesso.'''

users: list[str] = ["admin", "Mariella", "Jarod"]

for i in users:
    if i == "admin":
        print("ciao admin, vuoi vedere un rapporto sullo stato ?")

    if i == "Mariella":
        print("Ciao Mariella, grazie per aver effettuato nuovamente l'accesso")
        
    if i == "Jarod":
        print("Ciao Jarod, grazie per aver effettuato nuovamente l'accesso")

