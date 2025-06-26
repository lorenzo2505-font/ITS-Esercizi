from __future__ import annotations

from custom_types import *

from persona import Persona

from datetime import date

from impiegato import Impiegato

from resp_prog import resp_prog



class Progetto:

    _nome: str # noto alla nascita

    _impiegati: dict[Impiegato, resp_prog._link]  # da associazione 'coinvolto' [0..*], certamente non noto alla nascita

    def __init__(self, nome: str):
        
        self.setNome(nome)

        self._impiegati = dict()
    
    
    def nome(self):

        return self._nome
    
    def _add_link_resp_prog(self, l: resp_prog._link):
        
        if l.impiegato() in self._impiegati:
            raise KeyError("l'impiegato è già responsabile di questo progetto")
        
        if l.impiegato().is_responsabile() == False:
            raise KeyError("l'impiegato non ha la responsabilità per la gestione di progetti")
        
        self._impiegati[l.impiegato()] = l
    
    def _remove_link_coinvolto(self, l: resp_prog._link):

        if l.impiegato() not in self._impiegati:
            raise KeyError(f"l'impiegato non aveva la responsabilità su questo progetto")
        
        if l.impiegato().is_responsabile() == False:

            raise KeyError("l'impiegato non ha la responsabilità sulla gestione di progetti, ergo è escluso a priori")
        
        del self._impiegati[l.impiegato()]
    
    def impiegati(self) -> frozenset[resp_prog._link]:
        return frozenset(self._impiegati.values())
    
    def is_resp_prog(self, impiegato: Impiegato) -> bool:

        return impiegato in self._impiegati

    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    
    def __str__(self):
        
        return f"{self._nome}"


    


