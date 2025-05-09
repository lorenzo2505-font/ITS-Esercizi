'''8-11. Messaggi archiviati: inizia con il tuo lavoro dall'esercizio 8-10. 
Chiama la funzione send_messages() con una copia dell'elenco dei messaggi.
 Dopo aver chiamato la funzione, stampa entrambi gli elenchi per mostrare che l'elenco originale ha mantenuto i suoi messaggi'''



mylist: list[str] = ["da grandi poteri derivano grandi responsabilità", "ha un'aura potentissima", "che la forza sia con te"]

def show_messages (frasi: list[str]):
    for i in frasi:
        print(i)

'''show_messages(mylist)'''

def send_messages(mess: list[str]):
    sent_message: list[str] = []
    for i in mess:
        print(i)
        sent_message.append(i)
    print(sent_message)

send_messages(mylist)

print(mylist)
