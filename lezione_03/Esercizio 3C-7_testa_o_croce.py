'''Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".'''


numero_lanci: int = 0

cont_testa = 0
cont_croce = 0
while numero_lanci < 8:
    moneta: str = input("lancia la moneta: ")
    
    match moneta:
        case "t"|"T":
            numero_lanci+=1
            cont_testa+=1
        case "c"|"C":
            numero_lanci+=1
            cont_croce+=1
        case _:
            print("errore")

percentuale_testa = cont_testa * 100 / numero_lanci
percentuale_croce = cont_croce * 100 / numero_lanci

print(f"hai inserito la testa {cont_testa} volte, la percentuale è {percentuale_testa:.2f}%")
print(f"hai inserito la croce {cont_croce} volte, la percentuale è {percentuale_croce:.2f}%")

####




