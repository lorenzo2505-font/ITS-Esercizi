from __future__ import annotations

from custom_types import *

from persona import Persona

from datetime import date

from progetto import Progetto

from resp_prog import resp_prog

from posizione_militare import PosizioneMilitare



class Impiegato(Persona):

    _stipendio: RealGEZ # noto alla nascita

    _ruolo: Ruolo # noto alla nascita

    _is_responsabile: bool # certamente non noto alla nascita

    _progetti: dict[Progetto, resp_prog._link] # da associazione 'coinvolto' [0..*], certamente non noto alla nascita

    def __init__(self, *, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, genere: Genere, maternità: IntGEZ|None = None, posizione_militare: PosizioneMilitare|None = None, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool = False):

        super().__init__(nome=nome, cognome=cognome, cf=cf, nascita=nascita, genere=genere, maternità=maternità, posizione_militare=posizione_militare)

        self.setStipendio(stipendio)

        self.setRuolo(ruolo)

        self.setIsResponsabile(is_responsabile)

        self._progetti = dict()

        

    
    def stipendio(self):

        return self._stipendio
    
    def ruolo(self):

        return self._stipendio
    
    def is_responsabile(self):

        return self._is_responsabile
    
    def _add_link_resp_prog(self, l: resp_prog._link):

        if l.impiegato() != self:

            raise ValueError(f"il link non coinvolge me, ma {l.impiegato()}")

        if l.progetto() in self._progetti:

            raise KeyError(f"l'impiegato è già responsabile di questo progetto")

        if self.is_responsabile() == False:

            raise Exception(f"l'impiegato non ha la responsabilità su un progetto")
        
        
        self._progetti[l.progetto()] = l
    
    def _remove_link_resp_prog(self, l: resp_prog._link):

        if l.impiegato() != self:
            raise ValueError(f"il link non coinvolge me, ma {l.impiegato()}")

        if l.progetto() not in self._progetti:
            
            raise KeyError("l'impiegato non è responsabile di questo progetto")
        
        if self.is_responsabile() == False:

            raise Exception("l'impieagto non ha la responsabilità su nessun progetto, ergo è escluso a priori")
        
        del self._progetti[l.progetto()]

        
    
    def progetti(self) -> frozenset[resp_prog._link]:
        return frozenset(self._progetti.values())
    
    def is_resp_prog(self, progetto: Progetto) -> bool:
        return progetto in self._progetti

    
    def setStipendio(self, stipendio: RealGEZ):

        self._stipendio = stipendio
    
    def setRuolo(self, ruolo: Ruolo):

        self._ruolo = ruolo
    
    def setIsResponsabile(self, is_responsabile: bool):

        if (self._ruolo == Ruolo.segretario or self._ruolo == Ruolo.direttore) and (is_responsabile == True):

            raise ValueError("direttori o segretari non possono essere responsabili di un progetto")
        
        self._is_responsabile = is_responsabile
    
    def __str__(self):
        return super().__str__() + f",\nstipendio: {self._stipendio}, ruolo: {self._ruolo}"
    







    

