'''-2. Più test condizionali: non è necessario limitare il numero di test creati
mangiato fino a 10. Se vuoi provare più confronti, scrivi più test e aggiungili

a condizionale_tests.py. Ottieni almeno un risultato Vero e uno Falso per ciascuno di essi
quanto segue:
• Test di uguaglianza e disuguaglianza con stringhe
• Test utilizzando il metodo lower()
• Test numerici che coinvolgono uguaglianza e disuguaglianza, maggiore e minore
di, maggiore o uguale a e minore o uguale a
• Test utilizzando la parola chiave e e la parola chiave o
• Verificare se un elemento è in un elenco
• Verificare se un elemento non è presente in un elenco'''

assigment: bool
parola = str(input("inserisci parola: "))
if parola[0] == parola[-1]:
    print("la parola inizia e finisce con la stessa lettera")
    assigment = True
    print(assigment)
else:
    print("la parola NON inizia e finisce con la stessa lettera")
    assigment = False
    print(assigment)

dolce = str(input("inserisci dolce: "))
if dolce == "Maritozzo":
    print(dolce.lower())
    assigment = True
    print(assigment)

else:
    print("buono")
    assigment = False 
    print(assigment)

n = int(input("inserisci numero: "))
if n == 22:
    print("hai inserito il numero magico")
    assigment = True
    print(assigment)
if n != 22:
    print("perché non hai inserito il numero magico ?")
    assigment = False
    print(assigment)
if n == 13:
    print("deve essere venerdì")
if n > 0:
    print("il numero è positivo")
if n < 0:
    print("il numero è negativo")
if n >= 2:
    print("vedo che non hai inserito 1")
if n <= 1:
    print("hai poca fantasia, oppure sei molto NEGATIVO")
if (n % 2 == 0) and (n % 4 == 0):
    print("il numero è divisibile sia per due che per 4")
if (n == 88) or (n == 39):
    print("sembri un po' nostalgico")

frutta: list[str] = ["Banane", "Mele", "Arance", "Pesche", "Uva"]

string_test = str(input("inserisci: "))

'''for i in frutta:
    if string_test == i:
        print("la parola è anche nella lista")
        break

    else:
        print("la parola non è nella lista")
        break'''
if string_test in frutta:
    print("la parola è nella lista")
else:
    print("la parola non è nella lista")

    #git è tornato a funzionare 
    #sarai riuscito a funzionare ?
    #oggi funzioni ?####à



