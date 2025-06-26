from custom_types import *

from impiegato import Impiegato

from persona import Persona

from posizione_militare import PosizioneMilitare

from progetto import Progetto

from resp_prog import resp_prog

from studente import Studente

from datetime import date


lorenzo: Impiegato = Impiegato(nome = "lorenzo", 
                               cognome = "acomanni", 
                               cf = "SFQDZS37M20L545N", 
                               nascita = date(2005, 3, 25), 
                               posizione_militare = PosizioneMilitare("estente"), 
                               stipendio = 2000.0, 
                               ruolo = Ruolo("progettista"),
                               is_responsabile = True)


ristobook: Progetto = Progetto("ristobook")