from __future__ import annotations

from custom_types import *

from persona import *

from datetime import date



class Studente(Persona):

    _matricola: Matricola # <<immutable>> noto alla nascita

    def __init__(self, *, nome, cognome, cf, nascita, genere, maternità = None, posizione_militare = None, matricola: Matricola):
        super().__init__(nome=nome, cognome=cognome, cf=cf, nascita=nascita, genere=genere, maternità=maternità, posizione_militare=posizione_militare)

        self._matricola = matricola

            
        


    def matricola(self):

        return self._matricola
    
    def __str__(self):
        return super().__str__() + f",\nmatricola: {self._matricola}"
    

#lorenzo: Studente = Studente(nome = "lorenzo", cognome = "acomanni", cf = "CMNLNZ05C25H501J", nascita = date(2005, 3, 25), genere = Genere.uomo, posizione_militare = PosizioneMilitare("esente"), matricola = 12345678)



