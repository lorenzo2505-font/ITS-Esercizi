'''Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"'''

voto = int(input("inserisci voto: "))

match voto:
    case 10:
        print(f"{voto}: Eccellente")
    case 8|9:
        print(f"{voto}: Molto buono")
    case 6|7:
        print(f"{voto}: Sufficiente")
    case 4|5:
        print(f"{voto}: Insufficiente")
    case 1|2|3:
        print(f"{voto}: Gravemente insufficiente")
    case _:
        print("Voto non valido")