'''5-9. Nessun utente: aggiungi un test if a hello_admin.py per assicurarti che l'elenco degli utenti non sia vuoto.
• Se la lista è vuota, stampa il messaggio Dobbiamo trovare degli utenti!
• Rimuovere tutti i nomi utente dall'elenco e assicurarsi che venga stampato il messaggio corretto.'''

users: list[str] = []

for i in users:
    
    if i == "admin":
        print("ciao admin, vuoi vedere un rapporto sullo stato ?")
    if i == "Mariella":
        print("Ciao Mariella, grazie per aver effettuato nuovamente l'accesso")
    if i == "Jarod":
        print("Ciao Jarod, grazie per aver effettuato nuovamente l'accesso")

if len(users) == 0:
    print("dobbiamo trovare degli utenti")
    
        
        
