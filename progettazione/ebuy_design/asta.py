from __future__ import annotations
from typing import TYPE_CHECKING
from custom_types import *
from datetime import *
from post_oggetto import PostOggetto

if TYPE_CHECKING:
    from bid import Bid
    from privato import Privato

from asta_bid import asta_bid



class Asta(PostOggetto):

    _prezzo_bid: RealGZ # noto alla nascita

    _scadenza: datetime # noto alla nascita

    _bids: dict[Bid, asta_bid._link] # da associazione 'asta_bid' [0..*], certamente non noto alla nascita

    def __init__(self, *, descrizione: str, pubblicazione: datetime, anni_garanzia: IntGEZ, prezzo: RealGEZ, is_nuovo: bool, condizione: Condizione|None = None, prezzo_bid: RealGZ, scadenza: datetime):
        super().__init__(descrizione=descrizione, pubblicazione=pubblicazione, anni_garanzia=anni_garanzia, prezzo=prezzo, is_nuovo=is_nuovo, condizione=condizione)

        self.setPrezzoBid(prezzo_bid)

        self.setScadenza(scadenza)

        self._bids = dict()
    

    def prezzo_bid(self):

        return self._prezzo_bid
    
    def scadenza(self):

        return self._scadenza
    
    def _add_link_asta_bid(self, l: asta_bid._link):

        if l.asta() != self:
            raise ValueError(f"il link non coinvolge me, ma {l.asta()}")
        
        if l.bid() in self._bids:
            
            raise KeyError("il bid su quest'asta, è già stato fatto")
        
        self._bids[l.bid()] = l
    
    def _remove_link_asta_bid(self, l: asta_bid._link):

        if l.asta() != self:

            raise ValueError(f"il link non coinvolge me, ma {l.asta()}")
        
        if l.bid() not in self._bids:
            
            raise KeyError(f"non è stato mai fatto questo bid a quest'asta")
        
        del self._bids[l.bid()]

    def bids(self) -> frozenset[asta_bid._link]:
        return frozenset(self._bids.values())
    
    def asta_bid(self, bid: Bid) -> bool:

        return bid in self._bids
    
    def setPrezzoBid(self, prezzo_bid: RealGZ):

        if prezzo_bid <= self._prezzo:

            raise ValueError("il prezzo del bid deve essere superiore al prezzo di base")
        
        self._prezzo_bid = prezzo_bid
    
    def setScadenza(self, scadenza: datetime):
        
        if scadenza <= self._pubblicazione:

            raise ValueError("la scadenza deve essere oltre l'orario di pubblicazione")
        
        self._scadenza = scadenza
    
    def __str__(self):
        return super().__str__() + f"\nprezzo_bid: {self._prezzo_bid}\nscadenza: {self._scadenza}"
    
    def prezzo(i: datetime) -> RealGEZ:
        pass

    def vincitore(self) -> Privato|None:
        
        if not self.conclusa():

            raise ValueError("l'asta non è conclusa")
        
        ultimo_bid = self.ultimo_bid()

        return ultimo_bid._bid_ut_link.privato()

    def conclusa(self) -> bool:
        
        if self.scadenza() <= datetime.now():

            return True
        
        return False
    

    def ultimo_bid(self) -> Bid|None:
        
        max_b = self._bids[list(self._bids.keys()[0])]

        for l in self._bids.values():

            if l.bid().istante() > max_b.istante():

                max_b = l.bid()
            
            return max_b






        


