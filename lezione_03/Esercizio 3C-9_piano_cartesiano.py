'''Esercizio 3C-9. Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) 
e salvi le coordinate inserite in una tupla. Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."'''

point: tuple = ()

x: int = input("inserisci x: ")
y: int = input("inserisci y: ")

point = point + (x, y)

match point:
    case (x, 0):
        print("il punto si trova sull'asse x")
    case (0, y):
        print("il punto si trova sull'asse y")
    case point if point[0] > 0 and point[1] > 0:
        print("il punto si trova nel primo quadrante")
    case point if point[0] < 0 and point[1] > 0:
        print("il punto si trova nel secondo quadrante")
    case point if point[0] < 0 and point[1] < 0:
        print("il punto si trova nel terzo quadrante")
    case point if point[0] > 0 and point[1] < 0:
        print("il punto si trova nel quarto quadrante")

#quando devo imporre una struttura faccio una tupla 
#############




