'''8-9. Messaggi: crea un elenco contenente una serie di brevi messaggi di testo. 
Passa l'elenco a una funzione chiamata show_messages(), che stampa ogni messaggio di testo.'''

mylist: list[str] = ["da grandi poteri derivano grandi responsabilità", "ha un'aura potentissima", "che la forza sia con te"]

def show_messages (frasi: list[str]):
    for i in frasi:
        print(i)

show_messages(mylist)