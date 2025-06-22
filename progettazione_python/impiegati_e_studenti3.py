from custom_types import *

from datetime import date 

class Persona:

    _nome: str # noto alla nascita 

    _cognome: str # noto alla nascita

    _cf: CodiceFiscale # <<immutable>> noto alla nascita

    _nascita: date # <<immutable>> noto alla nascita

    _maternità: int|None # non noto alla nascita

    _genere: Genere # noto alla nascita


    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, maternità: int|None, genere: Genere):

        self.setNome(nome)

        self.setCognome(cognome)

        self._cf = cf

        self._nascita = nascita

        self.setMaternità(maternità)

        self._genere = genere

    
    def nome(self) -> str:

        return self._nome 
    
    def cognome(self) -> str:

        return self._cognome
    
    def cf(self) -> CodiceFiscale:

        return self._cf
    
    def nascita(self):

        return self._nascita
    
    def maternità(self) -> int|None:

        return self._maternità
    
    def genere(self) -> Genere:

        return self._genere 
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    

    def setCognome(self, cognome: str):

        if cognome:

            self._cognome = cognome
        
        else:

            raise ValueError("inserire un cognome valido")
    
    def setMaternità(self, maternità: int|None):

        if self._genere == Genere.uomo or maternità < 0:

            self._maternità = None
        
        else:

            self._maternità = maternità






class Studente(Persona):

    _matricola: IntGZ # <<immutable>>, noto alla nascita



    def __init__(self, nome, cognome, cf, nascita, maternità, genere, matricola: int):
        super().__init__(nome, cognome, cf, nascita, maternità, genere)

        self._matricola = matricola

        
    def matricola(self):

        return self._matricola 







    

class Impiegato(Persona):

    _stipendio: RealGEZ # noto alla nscita

    _ruolo: Ruolo # noto alla nascita

    _is_responsabile: bool|None # non noto alla nascita


    def __init__(self, nome, cognome, cf, nascita, maternità, genere, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool|None):
        super().__init__(nome, cognome, cf, nascita, maternità, genere)

        self.setStipendio(stipendio)

        self.setRuolo(ruolo)

        self.setIsResponsabile(is_responsabile)
    
    def stipendio(self):

        return self._stipendio
    
    def ruolo(self):

        return self._ruolo
    
    def is_responsabile(self):

        return self._is_responsabile
    
    def setStipendio(self, stipendio: RealGEZ):

        if stipendio:

            self._stipendio = stipendio
        
        else:

            raise ValueError("inserire un valore per lo stipendio valido")
    
    def setRuolo(self, ruolo: Ruolo):

        if ruolo:

            self._ruolo = ruolo
        
        else:

            raise ValueError("inserire un ruolo valido")
    
    
        



    





    