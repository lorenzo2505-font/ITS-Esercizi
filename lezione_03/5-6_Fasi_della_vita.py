'''5-6. Fasi della vita: scrivi una catena if-elif-else che determina la fase della vita di una persona.
 Imposta un valore per la variabile età, quindi:
• Se la persona ha meno di 2 anni, stampa un messaggio che informa che la persona è un neonato.
• Se la persona ha almeno 2 anni ma meno di 4, stampa un messaggio che la persona è un bambino.
• Se la persona ha almeno 4 anni ma meno di 13, stampa un messaggio che la persona è un bambino.
• Se la persona ha almeno 13 anni ma meno di 20, stampa un messaggio che la persona è un adolescente.
• Se la persona ha almeno 20 anni ma meno di 65, stampa un messaggio che la persona è maggiorenne.
• Se la persona ha 65 anni o più, stampa un messaggio che informa che la persona è un anziano.'''

età: int = 65

if età >= 0 and età < 2:
    print("neonato")
elif (età >= 2) and (età < 4):
    print("bambino")
elif (età >= 4) and (età < 13):
    print("bambino")
elif (età >= 13) and (età < 20):
    print("adolescente")
elif (età >= 20) and (età < 65):
    print("maggiorenne")
elif età < 0:
    print("ma non sei nenache nato")
else:
    print("anziano")