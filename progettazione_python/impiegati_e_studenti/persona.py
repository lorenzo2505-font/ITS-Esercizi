from __future__ import annotations

from custom_types import *

from posizione_militare import *

from datetime import date


class Persona:

    _nome: str # noto alla nascita

    _cognome: str # noto alla nascita

    _cf: CodiceFiscale # <<immutable>> noto alla nascita

    _nascita: date # <<immutable>> noto alla nascita

    _maternità: IntGEZ|None # certamente non noto alla nascita

    _genere: Genere #noto alla nascita

    _posizione_militare: PosizioneMilitare # certamente non noto alla nascita

    def __init__(self, *,
                 nome: str, 
                 cognome: str, 
                 cf: CodiceFiscale,
                  nascita: date,
                  genere: Genere,
                   maternità: IntGEZ|None = None,
                   posizione_militare: PosizioneMilitare|None = None):
        
        self.setNome(nome)
        
        self.setCognome(cognome)

        self._cf = cf

        self._nascita = nascita

        self.setGenere(genere)

        self.setMaternità(maternità)

        

        self.setPosizioneMilitare(posizione_militare)

        



    def nome(self) -> str:

        return self._nome
    
    def cognome(self) -> str:

        return self._cognome
    
    def cf(self) -> CodiceFiscale:

        return self._cf
    
    def nascita(self) -> date:

        return self._nascita
    
    def maternità(self) -> IntGEZ|None:

        return self._maternità
    
    def genere(self) -> Genere:

        return self._genere
    
    def posizione_militare(self):

        return self._posizione_militare
    
    def setNome(self, nome: str):

        if len(nome) < 2:

            raise ValueError("inserire un nome valido")
        
        self._nome = nome
    
    def setCognome(self, cognome: str):

        if len(cognome) < 2:

            raise ValueError("inserire un cognome valido")
        
        self._cognome = cognome
    
  
    
    def setMaternità(self, maternità:IntGEZ|None):

        if (self._genere == Genere.uomo) and (type(maternità) == IntGEZ):

            raise ValueError("un uomo non ha un numero di maternità")
        
        elif (self._genere == Genere.donna) and (maternità == None):

            raise ValueError("una donna deve avere un numero di maternità anche se è 0")
        
        self._maternità = maternità
    
    def setGenere(self, genere: Genere):

        self._genere = genere
    
   
    
    def setPosizioneMilitare(self, posizione_militare: PosizioneMilitare|None):
        

        if (self._genere == Genere.donna) and (type(posizione_militare) == PosizioneMilitare):

            raise ValueError("le donne in questo sistema non hanno una posizione militare")
        
        elif (self._genere == Genere.uomo) and (posizione_militare == None):

            raise ValueError("l'uomo deve avere una posizione militare")
        
        self._posizione_militare = posizione_militare
    
    def __str__(self):
        
        if self._genere == Genere.uomo:

            return f"nome: {self._nome}, cognome: {self._cognome}, codice fiscale: {self._cf}, data di nascita: {self._nascita}, genere: {self._genere}, posizione militare: {self._posizione_militare}"
        
        else:

            return f"nome: {self._nome}, cognome: {self._cognome}, codice fiscale: {self._cf}, data di nascita: {self._nascita}, genere: {self._genere}, numero di maternità: {self._maternità}"





#lorenzo: Persona = Persona(nome = "lorenzo", cognome = "acomanni", cf = "CMNLNZ05C25H501J", nascita = date(2005, 3, 25), genere = Genere.uomo, posizione_militare = PosizioneMilitare("esente"))








    
    
    

    
    


    
    
    
    
    

        
        
        
        
    


    





    
