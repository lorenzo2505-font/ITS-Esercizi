from typing import Any
from typing import Self

from enum import *


class Genere ():

    uomo = auto()
    
    donna = auto()

class Continente():

    pass

class Voto(int): 

    def __new__(cls, v: int|float|Self) -> Self:

        if v < 18 or v > 30:

            raise Exception(f"value v == {v} must be betweem 18 and 30")


class Indirizzo:

    _via: str
    _civico: int

    def __init__(self, via: str, civico: str):

        self._via = via

        self._civico= civico

    def get_via(self):

        return self._via
    
    def get_indirizzo(self):

        return self._civico
    
    def __hash__(self):

        return hash ((self._via, self._civico))
    
    def __eq__(self, other: Any):

        if other is None or not isinstance(other, type(self) or hash(self) != hash(other)):

            return False
        
        return self._via == other._via and self._civico == other._civico
    

class Codice_Fiscale:

    pass
        


        
    
        
        

          



class Persona (object):

    nome: str
    cf: str


    

    def __new__(cls, *args, **kwargs) -> Self:
        return super.__new__(cls)

    def __init__(self, nome: str, cf: str):

        self.nome = nome

        self.cf = cf

        

    
    def __eq__(self, other: Any )-> bool:

        if not isinstance(other, Persona):

            return False
        
        return self.cf == other.cf
    
    def __hash__(self) -> int:

        return hash(self.cf)

    



alice1: Persona = Persona ("alice", "bianchi")

alice2: Persona = Persona ("alice", "bianchi")







        

