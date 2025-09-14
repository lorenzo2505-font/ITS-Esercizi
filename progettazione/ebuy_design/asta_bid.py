from __future__ import annotations
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from asta import Asta
    from bid import Bid

class asta_bid:

    ''' Link a responsabilità doppia, con gestione asimmetrica verso Bid.'''

    class _link:
        
        _asta: Asta # <<immutable>> noto alla nascita

        _bid: Bid # <<immutable>> noto alla nascita

        def __init__(self, asta: Asta, bid: Bid):
            
            self._asta = asta

            self._bid = bid
        
        def asta(self):
            
            return self._asta
        
        def bid(self):

            return self._bid
        
        def hash(self) -> int:

            return hash((self.asta(), self.bid()))
        
        def __eq__(self, other: Any) -> bool:
            
            if type(other) != type(self) or hash(self) != hash(other):

                return False
            
            return (self.asta(), self.bid()) == (other.asta(), other.bid())
            
            



        
        
        

