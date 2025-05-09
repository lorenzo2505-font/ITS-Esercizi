'''def serie (target: str = 3.14):''' #si può anche definire una funzione ma è irrilevante

#metodo prof con stringa
target: str = "3.14"

pi: float  = 0.0
segno: int = 1
denominatore: int = 1
contatore: int = 0

while True:
    pi += segno * (4 / denominatore)

    if str(pi)[:len(target)] == target:
        print(f"la serie converge a {pi} dopo {contatore} iterazioni")
        break
    segno *= -1
    denominatore += 2
    contatore  += 1


#altro metodo con float (fallito)

'''target: float = 3.14

pi: float = 0
segno: int = 1
denominatore: int = 1
contatore: int = 0

while pi < target:
    pi += segno * (4 / denominatore)
    segno *= -1
    denominatore += 2
    contatore += 1

print(f"la serie converge a {pi} dopo {contatore} iterazioni")'''



