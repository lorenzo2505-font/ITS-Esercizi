import re

from typing import Self

from typing import Any

from enum import *

# metodo 1 
class CodiceFiscale_Metodo1:

    '''gli oggetti di questa classe *contengono* una stringa
    che rispetta il formato del codice fiscale'''

    cf: str

    def __init__(self, cf: str):

        cff: str = cf.upper().strip() #rendo la stringa maiuscola e senza spazi
        
        if re.fullmatch(r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$", cff):

            self.cf = cff
        else:

            raise ValueError("non corrisponde allo standard")










class CodiceFiscale_Metodo2 (str):

    #gli oggetti di questa classe sono stringhe
    # stringhe che rispettano il formato del codice fiscale

    def __new__(cls, cf: str) -> Self:

        cff: str = cf.upper().strip()

        if re.fullmatch(r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$", cff):

            return super().__new__(cls, cf)
        
        raise ValueError(f"la stringa {cff} non è un codice fiscale valido")




class CAP(str):

    def __new__(cls, cap: str) -> Self:

        if re.fullmatch(r"^\d{5}$", cap):

            return super().__new__(cls, cap)
        
        raise ValueError(f"la stringa {cap} non è valida")


class RealGEZ(float):

    #tipo di dato specializzato reale >= 0

    def __new__(cls, v: float|int|str|bool|Self) -> Self:

        n: float = float.__new__(cls, v) # prova a converire in un float

        if n >= 0:

            return n
        
        raise ValueError(f"il valore {n} è negativo!")


class Valuta(str):

    def __new__(cls, v: str) -> Self:

        if re.fullmatch(r"^[A-Z]{3}$", v):

            return super().__new__(cls, v)
        
        raise ValueError (f"la stringa {v} non è un codice valido per la valuta")



class Denaro:

    #rappresenta il tipo di dato concettuale composto
    #con i seguenti campi:
    # -importo: Reale
    # -valuta_ Valuta

    _importo: float
    _valuta: float

    def __init__(self, imp: float, val: Valuta):


        self._importo = imp

        self._valuta = val

    
    def importo(self) -> float:

        return self._importo
    
    def valuta(self) -> Valuta:

        return self._valuta
    
    def __str__(self) -> str:

        return f"{self.importo()} {self.valuta()}"
    
    def __repr__(self) -> str:

        return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
    
    def __hash__(self) -> int:

        return hash((self.importo(), self.valuta()))
    
    def __eq__(self, other: Any)-> bool:

        if not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return self.importo() == other.importo() and self.valuta() == other.valuta()
    
    def __add__(self, other: Self):


        if self.valuta() != other.valuta():

            raise ValueError(f" non si possono sommare importi di valute diverse")
        
        somma: float = self.importo() + other.importo()

        return Denaro(somma, self.valuta())


class FloatDenaro (float):

    _valuta: Valuta

    def __new__(cls, imp: float, val: Valuta) -> Self:

        d = super().__new__(cls, imp)

        d._valuta = val

        return d


class Indirizzo:

    def __init__(self, via: str, civico: str):

        self._via: str = via



class PosM (Enum):


    assolto = auto ()

    esente = auto()

    dispensato = auto()


        
    

    
    
    



    





        






