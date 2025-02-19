'''Più ospiti: hai appena trovato un tavolo da pranzo più grande, quindi ora è disponibile più spazio. Pensa ad altri tre ospiti da invitare a cena.
• Inizia con il tuo programma dall'esercizio 3-4 o 3-5. Aggiungi una chiamata print() alla fine del tuo programma,
 informando le persone che hai trovato una tabella più grande.
• Utilizza insert() per aggiungere un nuovo ospite all'inizio della tua lista.
• Usa insert() per aggiungere un nuovo ospite al centro della tua lista.
• Usa append() per aggiungere un nuovo ospite alla fine della tua lista.
• Stampa una nuova serie di messaggi di invito, uno per ogni persona nell'elenco.'''

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


