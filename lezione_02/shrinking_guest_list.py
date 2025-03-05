'''Lista degli invitati sempre più ridotta: 
hai appena scoperto che il tuo nuovo tavolo da pranzo non arriverà in tempo per la cena e ora hai spazio solo per due ospiti.
• Inizia con il tuo programma dall'Esercizio 3-6. Aggiungi una nuova riga che stampi un messaggio che dice che puoi invitare solo due persone a cena.
• Usa pop() per rimuovere gli ospiti dalla tua lista uno alla volta finché rimangono solo due nomi nella tua lista.
 Ogni volta che selezioni un nome dalla tua lista, 
 stampa un messaggio per quella persona facendogli sapere che ti dispiace di non poterla invitare a cena.
• Stampa un messaggio a ciascuna delle due persone ancora presenti nella tua lista, facendo loro sapere che sono ancora invitate.
• Utilizzare del per rimuovere gli ultimi due nomi dall'elenco, in modo da avere un elenco vuoto. 
Stampa la tua lista per assicurarti di avere effettivamente una lista vuota alla fine del tuo programma.'''

bros: list = ["Antonio", "Valerio", "Massimiliano"]
'''for i in bros:
    print(f"Ciao {i} ti va di venire a cena da me ?")'''

print(f"Ciao {bros[0]} ti va di venire a cena da me ?")
print(f"Ciao {bros[1]} ti va di venire a cena da me ?")
print(f"Ciao {bros[2]} ti va di venire a cena da me ?")

print(f"{bros[2]} non può venire ")

bros.remove("Massimiliano")

bros.append("Augusto")

'''for j in bros:
    print(f"Ciao {j}, ti va di venire a cena da me ? ")'''

print(f"Ciao {bros[0]} ti va di venire a cena da me ?")
print(f"Ciao {bros[1]} ti va di venire a cena da me ?")
print(f"Ciao {bros[2]} ti va di venire a cena da me ?")

print("ho trovato un tavolo più grande")

bros.insert(len(bros)// 1, "Paolo")

bros.append("Thomas")

'''for z in bros: 
    print(f"Ciao {z} ti andrebbe di venire a cena da me ? ")'''

print(f"Ciao {bros[0]} ti va di venire a cena da me ?")
print(f"Ciao {bros[1]} ti va di venire a cena da me ?")
print(f"Ciao {bros[2]} ti va di venire a cena da me ?")
print(f"Ciao {bros[3]} ti va di venire a cena da me ?")
print(f"Ciao {bros[4]} ti va di venire a cena da me ?")


print("posso inviatare a cena solo due persone ")

print(f"mi dispiace {bros.pop(0)}, ma non posso più invitarti")
print(f"mi dispiace {bros.pop(1)}, ma non posso più invitarti")
print(f"mi dispiace {bros.pop(2)}, ma non posso più invitarti")

print(f"{bros[0]}, te sei ancora invitato")
print(f"{bros[1]}, te sei ancora invitato")

del bros [1]
del bros [0]
print(bros)

