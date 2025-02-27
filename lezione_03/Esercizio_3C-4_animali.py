'''Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, 
utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  
mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.'''

#prima versione(più macchinosa)
'''mammiferi: list[str] = []
rettili: list[str] = []
uccelli: list[str] = []
pesci: list[str] = []

animale = str(input("inserisci animale: "))

match animale:
    case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
        mammiferi.append(animale)
        print("questo animale è un mammifero")
        print(mammiferi)
    case "serpente"|"lucertola"|"tartaruga"|"coccodrillo":
        rettili.append(animale)
        print("questo animale è un rettile")
        print(rettili)
    case "aquila"|"pappagallo"|"gufo"|"falco":
        uccelli.append(animale)
        print("questo animale è un ucello")
        print(uccelli)
    case "squalo"|"trota"|"salmone"|"carpa":
        pesci.append(animale)
        print("questo animale è un pesce")
        print(pesci)
    case _:
        print("errore, l'animale non è nei nostri elenchi, oppure non siamo in grado di classificarlo")'''

#seconda versione(più efficiente)

mammiferi: list[str] = ["cane","gatto","cavallo","elefante","leone"]
rettili: list[str] = ["serpente","lucertola","tartaruga","coccodrillo"]
uccelli: list[str] = ["aquila","pappagallo","gufo","falco"]
pesci: list[str] = ["squalo","trota","salmone","carpa"]

animale = str(input("inserisci animale: "))

match animale:
    case animale if animale in mammiferi:
        print("questo animale è un mammifero")
    case animale if animale in rettili:
        print("questo animale è un rettile")
    case animale if animale in uccelli:
        print("questo animale è un uccello")
    case animale if animale in pesci:
        print("questo animale è un pesce")
    case _:
        print("errore, l'animale non è nei nostri elenchi, oppure non siamo in grado di classificarlo")



        



        