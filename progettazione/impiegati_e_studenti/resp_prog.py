from __future__ import annotations

from typing import Any

from custom_types import *

from datetime import date

from impiegato import Impiegato

from progetto import Progetto


class resp_prog:

    @classmethod

    def add(cls, impiegato: Impiegato, progetto: Progetto) -> _link:

        l = cls._link(impiegato, progetto)
        impiegato._add_link_resp_prog(l)
        progetto._add_link_resp_prog(l)
        return l # viene restituito il link creato
    
    @classmethod

    def remove(cls, l: _link) -> None:
        l.progetto()._remove_link_resp_prog(l)
        l.impiegato()._remove_link_resp_prog(l)
        del l # il link viene cancellato
        
        
        



    class _link:

        _impiegato: Impiegato # <<immutable>> noto alla nascita

        _progetto: Progetto # <<immutable>> noto

        def __init__(self, impiegato: Impiegato, progetto: Progetto):

            self._impiegato = impiegato

            self._progetto = progetto
        
        def impiegato(self) -> Impiegato:

            return self._impiegato
        
        def progetto(self) -> Progetto:

            return self._progetto
        
        def hash(self) -> int:

            return hash((self.impiegato(), self.progetto()))
        
        def __eq__(self, other: Any) -> bool:
            
            if type(other) != hash(other) or hash(self) != hash(other):

                return False
            
            return (self.impiegato(), self.progetto()) == (other.impiegato(), other.progetto())
            


        
        

            

            