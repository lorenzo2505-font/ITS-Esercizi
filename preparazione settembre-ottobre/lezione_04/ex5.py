'''5. Sistema di gestione dell'inventario:

Creare una lista per conservare gli articoli in inventario.

Creare una funzione che definisca un articolo con codice, nome, quantità e prezzo.

Implementare funzioni per aggiungere, rimuovere, cercare e aggiornare gli articoli in inventario.

Utilizzare cicli for per gestire le varie operazioni di inventario.'''


inventario: list[dict] = []


def definizioneArticolo(codice: str, nome: str, quantità: int, prezzo: float):
    
    return {"codice": codice, "nome": nome, "quantià": quantità, "prezzo": prezzo}

v1 = definizioneArticolo("1234", "cappello di pierlions", 1, 400.0)

#print(v1)

def aggiungiArticolo(inventario: list[dict], articolo: dict):

    if articolo in inventario:

        raise ValueError("l'articolo è già presente nell'inventario")
    
    inventario.append(articolo)

aggiungiArticolo(inventario, v1)

print(inventario)


def rimuoviArticolo(inventario: list[dict], articolo: dict):

    if articolo not in inventario:

        raise ValueError("l'articolo non è presente nell'inventario")
    
    inventario.remove(articolo)

'''rimuoviArticolo(inventario, v1)

print(inventario)'''


def cercaArticolo(inventario: list[dict], nome_articolo: str):

    for i in range(len(inventario)):
        
        if nome_articolo == inventario[i]["nome"]:
            
            return f"articolo trovato: {inventario[i]}"
    
    return f"l'articolo: {nome_articolo} non è nell'inventario"


#print(cercaArticolo(inventario, "cappello di pierlions"))

def aggiornaInventario(inventario: list[dict], articolo: dict,  codice: str = None, nome: str = None,  quantità: int = None, prezzo: float = None):

    index = None

    if articolo not in inventario:

        raise ValueError("l'articolo non è presente nell'inventario")
    
    for i in range(len(inventario)):

        if inventario[i] == articolo:
            
            index = i
            inventario.pop(index)
    
    if codice is not None:
        articolo["codice"] = codice
    
    if nome is not None:
        articolo["nome"] = nome
    
    if quantità is not None:
        articolo["quantità"] = quantità
    
    if prezzo is not None:
        articolo["prezzo"] = prezzo

    inventario.insert(index, articolo)

    return inventario


print(aggiornaInventario(inventario, v1, quantità = 2))





            

        
        
        


