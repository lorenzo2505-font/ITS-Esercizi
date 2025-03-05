'''Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, 
affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat.
 Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, 
 oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. 
 Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra'''

mammiferi: list[str] = ["cane","gatto","cavallo","elefante","leone", "balena", "delfino"]
rettili: list[str] = ["serpente","lucertola","tartaruga","coccodrillo"]
uccelli: list[str] = ["aquila","pappagallo","gufo","falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list[str] = ["squalo","trota","salmone","carpa"]

animal_type: str

animale:str = input("inserisci animale: ")
habitat: str = input("inserisci habitat")

match animale:
    case animale if animale in mammiferi:
        print("questo animale è un mammifero")
        animal_type = "mammifero"
    case animale if animale in rettili:
        print("questo animale è un rettile")
        animal_type = "rettile"
    
    case animale if animale in uccelli:
        print("questo animale è un uccello")
        animal_type = "uccello"
    case animale if animale in pesci:
        print("questo animale è un pesce")
        animal_type = "pesce"
    case _:
        print("errore, l'animale non è nei nostri elenchi, oppure non siamo in grado di classificarlo")
        animal_type = "unknown"

my_animal_dict: dict = {"nome": animale, "categoria": animal_type, "habitat": habitat}

match my_animal_dict:
    case {"nome": "cane", "categoria": "mammifero", "habitat": "terra"}:
        print("l'habitat è corente con l'animale")
    case {"nome": "cane", "categoria": "mammifero", "habitat": "aria"} | {"nome": "cane", "categoria": "mammifero", "habitat": "acqua"}:
        print("l'habitat non è corente con l'animale")

 
    #####