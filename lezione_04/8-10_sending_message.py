'''8-10. Invio di messaggi: inizia con una copia del tuo programma
 dall'esercizio 8-9. Scrivi una funzione chiamata send_messages() che stampa ogni messaggio di testo e sposta ogni messaggio 
 in una nuova lista chiamata sent_messages mentre viene stampata. 
 Dopo aver chiamato la funzione, stampa entrambe le tue liste per assicurarti che i messaggi siano stati spostati correttamente.'''


mylist: list[str] = ["da grandi poteri derivano grandi responsabilità", "ha un'aura potentissima", "che la forza sia con te"]

def show_messages (frasi: list[str]):
    for i in frasi:
        print(i)

'''show_messages(mylist)'''

def send_messages(mess: list[str]):
    sent_messages: list = []
    while mess:
        sent_messages.append(mess.pop(0))
    print(mess)
    print(sent_messages)
   

send_messages(mylist)





    





    