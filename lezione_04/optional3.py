'''Carrello e-commerce:

Crea una funzione che definisca un prodotto con nome, prezzo e quantità.

Crea funzioni che gestiscano il carrello, consentendo all'utente di aggiungere, rimuovere e visualizzare i prodotti nel carrello.

Crea una funzione che calcoli il totale del carrello e applichi eventuali sconti o tasse.

Crea una funzione per stampare un riepilogo dettagliato del carrello, inclusi prodotti e totali.

Implementa un ciclo for per scorrere gli articoli nel carrello e stampare informazioni dettagliate su ciascun prodotto e sul totale.'''

from typing import Any



def prodotto (nome: str = None, prezzo: float = None, quantità: int = None):

    p: dict = {"nome": nome, "prezzo": prezzo, "quantità": quantità}

    return p




def gestione_cartello():

    carrello: list[dict] = []

    opzioni: list = ["aggiungere", "rimuovere", "visualizzare", "chiudere"]

    while True:

        scelta = input("inserisci opzione: ")

        if scelta not in opzioni:

            print("errore, la scelta non rientra tra le opzioni disponibili, dovrai riavviare il programma")
            break

        else:

            if scelta == "chiudere":
                break

            if scelta == "aggiungere":

                aggiunta_prodotto = prodotto(str(input("inserisci nome: ")), float(input("inserisci prezzo: ")), int(input("inserisci quantità: ")))

                carrello.append(aggiunta_prodotto)
            
            if scelta == "rimuovere":

                n: int = int(input("inserisci indice "))

                for i in range(len(carrello)):

                    if i == n:
                        carrello.pop(i)
                    
                    else:
                        pass
            
            if scelta == "visualizzare":

                print(carrello)
    
    return carrello







def totale():

    temp1 = 0

    temp2 = 0

    lista_moltiplicazioni: list = []

    m = 1

    s = 0

   

    v = gestione_cartello ()

    

    for i in range(len(v)):

        for key, value in v[i].items():

            if key == "prezzo":

                temp1 = value
            
            if key == "quantità":

                temp2 = value

                m = temp1 * temp2

                lista_moltiplicazioni.append(m)
    
    s = sum(lista_moltiplicazioni)

    if len(v) >= 5:

        s = s * 50 / 100


    
    
    v.append({"prezzo totale": s})

    return v

    



def riepilogo ():

    opzioni = ["continuare", "basta"]

    while True:

        opzione = input("scegli opzione: ")

        if opzione not in opzioni:

            print("errore, il programma si fermerà")
            break

        if opzione == "basta":

            break

        if opzione == "continuare":

            t = totale()
    

            for i in range(len(t)):

                for key, value in t[i].items():

                    print(key, value)


riepilogo()

            












             







          
            



    



    
            






    



    

    

    

