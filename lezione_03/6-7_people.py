'''6-7. Persone: inizia con il programma che hai scritto per l'esercizio 6-1.
 Crea due nuovi dizionari che rappresentano persone diverse e memorizza tutti e tre i dizionari in un elenco chiamato persone. 
 Sfoglia l'elenco delle persone. Mentre scorri l'elenco, stampa tutto ciò che sai su ciascuna persona.'''

persona: dict = {"nome": "Lorenzo", "cognome": "Acomanni", "età": 19, "città": "Roma"}

amico1: dict  = {"nome": "Augusto", "cognome": "Ricci", "età": 19, "città": "Roma"}

amico2: dict  = {"nome": "Paolo", "cognome": "Nicita", "età": 19, "città": "Roma"}

people: list = [persona, amico1, amico2]

for i in range (len(people)):
    print(people[i])
    
    

