'''5-10. Controllo dei nomi utente: procedi come segue per creare un programma che simuli il modo in cui i siti Web
 garantiscono che tutti abbiano un nome utente univoco.
• Creare un elenco di cinque o più nomi utente chiamati current_users.
• Crea un altro elenco di cinque nomi utente chiamato new_users. Assicurati
 che uno o due dei nuovi nomi utente siano presenti anche nell'elenco current_users.
• Scorri l'elenco new_users per vedere se ogni nuovo nome utente è già stato utilizzato. 
In tal caso, stampa un messaggio in cui viene richiesto alla persona di inserire un nuovo nome utente.
 Se non è stato utilizzato un nome utente, stampa un messaggio dicendo che il nome utente è disponibile.
• Assicurati che il confronto non faccia distinzione tra maiuscole e minuscole. 
Se è stato utilizzato "John", "JOHN" non deve essere accettato. 
(Per fare ciò, dovrai creare una copia di current_users contenente le versioni in minuscolo di tutti gli utenti esistenti.)'''

current_user: list[str] = ["LORENZO", "thommy_marchio", "bozzo", "giumi_cassino", "luca_ischia_2003"]
new_user: list[str] = ["BOZZO", "bald_erald", "red_dioni", "rossi_bennington", "raponi_chad"]

for i in range(len(new_user)):
    if (new_user[0:i] == current_user[0:i]) or (new_user[0:i] == current_user[i].title()) or (new_user[0:i] == current_user[i].upper()) or (new_user[0:i] == current_user[i].lower()): 
            print("inserisci di nuovo il nome  utente")
    else:
        print("nome utente valido")




    
        

