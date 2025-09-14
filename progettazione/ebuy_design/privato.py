from __future__ import annotations
from typing import TYPE_CHECKING
from utente import Utente
from datetime import *

if TYPE_CHECKING:
    from bid import Bid

from bid_ut import bid_ut


class Privato(Utente):

    _bids: dict[Bid, bid_ut._link] # da associazione 'bid_ut' [0..*], non noto alla nascita

    def __init__(self, username: str, registrazione: datetime):
        super().__init__(username, registrazione)

        self._bids = dict()
    
    def _add_link_bid_ut(self, l: bid_ut._link):

        if l.privato() != self:
            
            raise ValueError(f"il link non coinvolge me, ma {l.privato()}")
        
        if l.bid() in self._bids:

            raise KeyError("il bid è stato già fatto")
        
        self._bids[l.bid()] = l
    
    def _remove_link_bid_ut(self, l: bid_ut._link):

        if l.privato() != self:

            raise ValueError(f"il link non coinvolge me, ma {l.privato()}")
        
        if l.bid() not in self._bids:
            
            raise KeyError("l'utente non ha mai fatto il bid")
        
        del self._bids[l.bid()]

    
    def bids(self) -> frozenset[bid_ut._link]:

        return frozenset(self._bids.values())
    
    def bid_ut(self, bid: Bid) -> bool:

        return bid in self._bids
    
        

