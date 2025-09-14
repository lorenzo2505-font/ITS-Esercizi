from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import *
from custom_types import *

class PostOggetto(ABC):

    _descrizione: str # noto alla nascita

    _pubblicazione: datetime # <<immutable>>, noto alla nascita

    _anni_garanzia: IntGEZ # noto alla nascita

    _prezzo: RealGEZ # noto alla nascita

    _is_nuovo: bool # <<immutable>>, noto alla nascita

    _condizione: Condizione|None # <<immutable>>, noto alla nascita

    def __init__(self, *, descrizione: str,
                  pubblicazione: datetime,
                  anni_garanzia: IntGEZ,
                  prezzo: RealGEZ,
                  is_nuovo: bool,
                  condizione: Condizione|None = None):
        
        super().__init__()

        self.setDescrizione(descrizione)
        
        self._pubblicazione = pubblicazione

        self.setAnniGaranzia(anni_garanzia)

        self.setPrezzo(prezzo)

        self._is_nuovo = is_nuovo

        if self._is_nuovo and type(condizione) == Condizione:

            raise ValueError("gli oggetti nuovi non hanno una condizione")
        
        elif not(self._is_nuovo) and condizione == None:

            raise ValueError("gli oggetti usati devono avere una condizione") 
        
        self._condizione = condizione
    
    def descrizione(self):

        return self._descrizione
    
    def pubblicazione(self):

        return self._pubblicazione
    
    def anni_garanzia(self):

        return self._anni_garanzia
    
    def prezzo(self):

        return self._prezzo
    
    def is_nuovo(self):

        return self._is_nuovo
    
    def condizione(self):

        return self._condizione
    
    def setDescrizione(self, descrizione: str):

        if descrizione:

            self._descrizione = descrizione 
        
        else:

            raise ValueError("inserire una descrizione valida")
    
    def setAnniGaranzia(self, anni_garanzia: IntGEZ):

        self._anni_garanzia = anni_garanzia
    
    def setPrezzo(self, prezzo: RealGEZ):

        self._prezzo = prezzo
    
    def __str__(self):
        return super().__str__() + f"descrizione: {self._descrizione}\npubblicazione: {self._pubblicazione}\nanni di garanzia: {self._anni_garanzia}\n prezzo: {self._prezzo}$\nè nuovo ?: {self._is_nuovo}, condizione: {self._condizione}"



    

    



