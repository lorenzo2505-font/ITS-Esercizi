'''6-3. Glossario: un dizionario Python può essere utilizzato per modellare un dizionario reale. Tuttavia, per evitare confusione, chiamiamolo glossario.
• Pensa a cinque parole di programmazione che hai imparato nei capitoli precedenti. Usa queste parole come chiavi nel tuo glossario e memorizza i loro significati come valori.
• Stampa ogni parola e il suo significato come output ben formattato.
 Potresti stampare la parola seguita da due punti e poi il suo significato, 
 oppure stampare la parola su una riga e poi stampare il suo significato rientrato su una seconda riga.
 ù Utilizza il carattere di nuova riga (\n) per inserire una riga vuota tra ciascuna coppia di significati di parole nell'output.'''

glossario: dict = {"print": "utilizzato per stampare in output qualsisasi tipo di messaggio", 
                   "append": "utilizzato per aggiungere nuovi  elementi in una lista",
                   "while":  "ripetono un istruzione di codice fino a quando essa rimane vera",
                    "if": "permette di eseguire diversi blocchi di codice in base alle condizioni", 
                    "is": "operatore d'identità che consente di fare dei confronti"}

for key, value in glossario.items():
    print(f"questo è il comando {key}: \n {value}")
