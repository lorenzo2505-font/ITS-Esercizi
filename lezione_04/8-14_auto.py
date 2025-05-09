'''8-14. Auto: 
scrivi una funzione che memorizzi informazioni su un'auto in un dizionario.
La funzione dovrebbe sempre ricevere un produttore e un nome di modello.
Dovrebbe quindi accettare un numero arbitrario di argomenti di parole chiave.
Chiama la funzione con le informazioni richieste e altre due coppie nome-valore, come un colore o una caratteristica opzionale.
La tua funzione dovrebbe funzionare per una chiamata come questa: car = make_car('subaru', 'outback', color='blue', tow_package=True)
Stampa il dizionario restituito per assicurarti che tutte le informazioni siano state memorizzate correttamente.'''

def car(produttore: str, modello: str, colore: str, caratteristica):
    return {"produttore": produttore, "modello": modello, "colore": colore, "caratteristica": caratteristica}

catch_dict: dict = car ("fiat", "panda", "grigio", "usata nelle autoscuole")
print(catch_dict)
###