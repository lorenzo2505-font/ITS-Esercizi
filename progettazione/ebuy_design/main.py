from datetime import datetime
from custom_types import *

#  classi base
from utente import Utente
from post_oggetto import PostOggetto

#  classi di associazione
from asta_bid import asta_bid
from bid_ut import bid_ut

#  classi principali
from asta import Asta
from privato import Privato
from bid import Bid



def main():

    p: Privato = Privato("loreacomanni2005", datetime(2017, 6, 12, 14, 30, 0))

    a: Asta = Asta(descrizione = "questa è la macchina di popa senza freni",
                   pubblicazione = datetime(2025, 7, 10, 19, 30, 0),
                   anni_garanzia = 2,
                   prezzo = 350.0,
                   is_nuovo = False,
                   condizione = Condizione.discreto,
                   prezzo_bid = 400.0,
                   scadenza = datetime(2025, 7, 31, 10, 00, 00))
    
    b: Bid = Bid(datetime(2025, 7, 15, 11, 57), a, p)

    print(a._bids)

    print(p._bids)



main()






