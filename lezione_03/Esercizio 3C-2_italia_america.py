'''Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0'''

voto = int(input("inserisci voto universitario italiano: "))
gpa: float
match voto:
    case voto if voto >= 106 and voto <= 110:
        gpa = 4.0
        print(f"GPA: {gpa}")
    case voto if voto >= 101 and voto <= 105:
        gpa = 3.7
        print(f"GPA: {gpa}")
    case voto if voto >= 96 and voto <= 100:
        gpa = 3.3
        print(f"GPA: {gpa}")
    case voto if voto >= 91 and voto <= 95:
        gpa = 3.0
        print(f"GPA: {gpa}")
    case voto if voto >= 86 and voto <= 90:
        gpa = 2.7
        print(f"GPA: {gpa}")
      
    case voto if voto >= 81 and voto <= 85:
        gpa = 2.3
        print(f"GPA: {gpa}")
    case voto if voto >= 76 and voto <= 80:
        gpa = 2.0
        print(f"GPA: {gpa}")
    case voto if voto >= 70 and voto <= 75:
        gpa = 1.7
        print(f"GPA: {gpa}")
    case voto if voto >= 66 and voto <= 69:
        gpa = 1.0
        print(f"GPA: {gpa}")
    case _:
        print("errore")
        


 
