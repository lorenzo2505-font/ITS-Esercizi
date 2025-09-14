from __future__ import annotations
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from bid import Bid
    from privato import Privato



class bid_ut:

    """ Link a responsabilità doppia con gestione asimmetrica verso Bid.
    """


    class _link:

        _bid: Bid # <<immutable>> noto alla nascita

        _privato: Privato # <<immutable>> noto alla nascita

        def __init__(self, bid: Bid, privato: Privato):
            
            self._bid = bid

            self._privato = privato
        
        def bid(self) -> Bid:

            return self._bid
        
        def privato(self) -> Privato:

            return self._privato
        
        def hash(self) -> int:

            return hash(self.bid(), self.privato())
        
        def __eq__(self, other: Any) -> bool:
            
            if type(other) != type(self) or hash(self) != hash(other):
                
                return False
            
            return (self.bid(), self.privato()) == (other.bid(), other.privato())
        
        