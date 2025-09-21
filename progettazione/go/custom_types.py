import re

from typing import Self 

from typing import Any

from enum import *




class CodiceFiscale (str):

    #gli oggetti di questa classe sono stringhe
    # stringhe che rispettano il formato del codice fiscale

    def __new__(cls, cf: str) -> Self:

        cff: str = cf.upper().strip()

        if re.fullmatch(r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$", cff):

            return super().__new__(cls, cf)
        
        raise ValueError(f"la stringa {cff} non è un codice fiscale valido")






class RealGEZ(float):

    #tipo di dato specializzato reale >= 0

    def __new__(cls, v: float|int|str|bool|Self) -> Self:

        n: float = float.__new__(cls, v) # prova a converire in un float

        if n >= 0:

            return n
        
        raise ValueError(f"il valore {n} è negativo!")





class CAP(str):

    def __new__(cls, cap: str) -> Self:

        if re.fullmatch(r"^\d{5}$", cap):

            return super().__new__(cls, cap)
        
        raise ValueError(f"la stringa {cap} non è valida")



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
    
    def __str__(self):
        
        return f"{self.via} {self.civico}"



class Email (str):

    def __new__(cls, email: str):

        if re.fullmatch(r"^\S+@\S+\.\S+$", email):

            return super().__new__(cls, email)
        
        else:

            raise ValueError("l'email deve rispettare lo specifico modello")
        
    def domain(self) -> str:
        """
        Restituisce la sottostringa che segue la chiocchiola ("@")"""
        pass



class Telefono (str):

    def __new__(cls, tel: str):

        if re.fullmatch(r"^\+?[1-9][0-9]{7,14}$", tel):

            return super().__new__(cls, tel)
        
        else:

            raise ValueError ("numero di telefono inserito non correttamente")




class CodiceVolo (str):

    def __new__(cls, volo: str):

        if re.fullmatch(r"\b[A-Z]{2}\d{3,4}\b", volo):

            return super().__new__(cls, volo)
        
        else:

            raise ValueError("inserire un codice di volo corretto")




class CodiceAereoporto (str):

    def __new__(cls, aereoporto: str):

        if re.fullmatch(r"\b[A-Z]{3}\b", aereoporto):

            return super().__new__(cls, aereoporto)
        
        else:

            raise ValueError("inserire un codice di volo valido")

class IntGEZ(int):

    def __new__(cls, v: float|int|str|bool|Self) -> Self:

        n: int = super().__new__(cls, v)

        if n >= 0:

            return n
        
        raise ValueError(f"il valore {n} è minore di 0")
        



class IntGZ (int):

    def __new__(cls, v: float|int|str|bool|Self) -> Self:

        n: int = super().__new__(cls, v)

        if n > 0:

            return n

        raise ValueError(f"il valore {n} non è positivo")



class Ruolo():

    segretario = auto()

    direttore = auto()

    progettista = auto()


class Komi(float):
    
    def __new__(cls, v: float|int|str|bool|Self) -> Self:
        n: float = super().__new__(cls, v)

        if 0 <= n <= 10:
            return n
        
        raise ValueError(f'il valore {n} non è compreso tra 0 e 10')



class Rinuncia(Enum):
    bianco = auto()
    nero = auto
