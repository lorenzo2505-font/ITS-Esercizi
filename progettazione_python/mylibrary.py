#questa è la mia libreria personalizzata dove verranno messe le varie classi che spesso andrò ad utilizzare in altri progetti



from enum import *

from typing import Self

from typing import Any

import time

import datetime




class Genere():

    uomo = auto ()

    donna = auto ()


class Voto (int):


    def __new__(cls, v: int|float|Self) -> Self:

        if v < 18 or v > 30:

            raise ValueError(f"Value v == {v} must be between 18 and 30")
        
        return int.__new__(cls, v)


class Indirizzo:

    def __init__(self, via: str, civico: int):

        self.via = via

        self.civico = civico

        
    
    def __hash__(self)->int:

        return hash( (self.via(), self.civico()) )
    
    def __eq__(self, other:Any)->bool:
        
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            
            return False
        
        return (self.via(), self.civico() ) == (other.via(), other.civico())

        



class Studente:

    def __init__(self, matricola: int, nome: str, genere: Genere, indirizzo: Indirizzo):
        
        self.matricola = matricola

        self.nome = nome

        self.genere = genere

        self.indirizzo = indirizzo



class Esame:

    def __init__(self, data: datetime.time, voto: Voto):
        
        self.data = data

        self.voto = voto


    
    




    

