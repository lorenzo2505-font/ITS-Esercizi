'''Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica),
 salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:'''



giorno: int = int(input("inserisci giorno: "))
mese: int = int(input("inserisci mese: "))
data: tuple = (giorno, mese)



match data:
    case(1, 1):
        print("Capodanno")
    case(14, 2):
        print("San Valentino")
    case (2, 2):
        print("Festa Repubblica Italiana")
    case (15, 8):
        print("Ferragosto")
    case (31, 10):
        print("Halloween")
    case (25, 12):
        print("Natale")
    case _:
        print("nessuna festività importante in questa data, oppure ne hai inserita una che è inesistente")


