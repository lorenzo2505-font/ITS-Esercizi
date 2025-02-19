'''Modifica dell'elenco degli invitati: hai appena saputo che uno dei tuoi ospiti 
non può partecipare alla cena, quindi devi inviare una nuova serie di inviti. Dovrai pensare a qualcun altro da invitare.
• Inizia con il tuo programma dall'Esercizio 3-4. Aggiungi una chiamata print() alla fine del tuo programma, indicando 
il nome dell'ospite che non potrà partecipare.
• Modifica la tua lista, sostituendo il nome dell'ospite che non potrà partecipare con il nome della nuova persona che stai invitando.
• Stampa una seconda serie di messaggi di invito, uno per ogni persona ancora presente nell'elenco.'''

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





