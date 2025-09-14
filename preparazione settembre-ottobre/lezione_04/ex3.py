'''3. Carrello e-commerce:

Creare una funzione che definisca un prodotto con nome, prezzo e quantità.

Creare funzioni che gestiscano il carrello, consentendo all'utente di aggiungere, rimuovere e visualizzare i prodotti nel carrello.

Creare una funzione che calcoli il totale del carrello e applichi eventuali sconti o tasse.

Creare una funzione per stampare un riepilogo dettagliato del carrello, inclusi prodotti e totali.

Implementare un ciclo for per scorrere gli articoli nel carrello e stampare informazioni dettagliate su ciascun prodotto e il totale.'''


def definizioneProdotto(nome: str, prezzo: float, quantità: int) -> dict:

    return {"nome": nome, "prezzo": prezzo, "quantità": quantità}


v1 = definizioneProdotto("canna del popa", 500.0, 2)
print(v1)

def aggiungiProdotto(carrello: list[dict], prodotto: dict) -> list[dict]:

    if prodotto in carrello:
        
        raise ValueError("il prodotto è già presente all'interno del carrello")

    carrello.append(prodotto)

    return carrello


v2 = aggiungiProdotto([], v1)
print(v2)


def rimuoviProdotto(carrello: list[dict], prodotto: dict) -> list[dict]:

    if prodotto not in carrello:

        raise ValueError("il prodotto non è presente all'interno del carrello")

    carrello.remove(prodotto)
    
    return carrello

'''v3 = rimuoviProdotto(v2, v1)
print(v3)'''

def visualizzaProdotti(carrello: list[dict]):

    for i in carrello:
        print[i]["nome"]



def totaleCarrello(carrello: list[dict]) -> float:

    prezzi_prodotti: list[float] = []

    for i in range(len(carrello)):

        if carrello[i]["prezzo"] > 50.0:
            carrello[i]["prezzo"] -= carrello[i]["prezzo"] * 10 / 100

        totale = carrello[i]["prezzo"] * carrello[i]["quantità"]
        prezzi_prodotti.append(totale)
    
    return sum(prezzi_prodotti)


def riepilogoCarrello(carrello: list[dict]):
    
    for i in range(len(carrello)):
        
        print(f"nome prodotto: {carrello[i]["nome"]}")
        print(f"prezzo: {carrello[i]["prezzo"]}")
        print(f"quantità: {carrello[i]["quantità"]}")

    print(f"totale carrello {totaleCarrello(carrello)}")
    
    


print(riepilogoCarrello(v2))








