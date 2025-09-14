from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import *

if TYPE_CHECKING:
    from asta import Asta
    from privato import Privato

from asta_bid import asta_bid
from bid_ut import bid_ut




class Bid:

    _istante: datetime # <<immutable>>, noto alla nascita

    _asta: asta_bid._link  # da associazione 'asta_bid' [1..1], <<immutable>> noto alla nascita

    _privato: bid_ut._link # da associazione 'bid_ut' [1..1], <<immutable>> noto alla nascita


    


    def __init__(self, istante: datetime, asta: Asta, privato: Privato):
        
        self._istante = istante

        self._add_link_asta_bid(asta)

        self._add_link_bid_ut(privato)

    
    def istante(self) -> datetime:

        return self._istante
    
    def _add_link_asta_bid(self, asta: Asta) -> None:
        l = asta_bid._link(asta, self)
        self._asta_bid_link = l
        asta._add_link_asta_bid(l)
    
    def _add_link_bid_ut(self, privato: Privato) -> None:
        l = bid_ut._link(self, privato)
        self._bid_ut_link = l
        privato._add_link_bid_ut(l)
    
    def __str__(self):
        
        return f"{self._istante}"
    

