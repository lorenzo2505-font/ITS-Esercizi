# azienda3 versione prof

from custom_types import *

from datetime import date


class Impiegato:

    _nome: str #noto alla nascita
    
    _cognome: str #noto alla nascita

    _nascita: date # <<immutable>>, noto alla nascita

    _stipendio: RealGEZ #noto alla nascita

    def __init__(self, nome: str, cognome: str, data: date, stipendio: RealGEZ):
        pass

    def nome(self) -> str:

        return self._nome
    
    def cognome(self) -> str:

        return self._cognome
    
    def nascita(self) -> date:

        return self._nascita
    
    def stipendio(self) -> RealGEZ:

        return self._stipendio





class Dipartimento:

    _nome: str # noto alla nascita

    _telefoni: set [str] # [1..*] (e quindi noto alla nascita)

    _indirizzo: Indirizzo # mutabile [0..1] certamente noto alla nascita


    def __init__(self, nome: str, telefono: str, indirizzo: Indirizzo | None):

        
        self.set_nome(nome)

        self._telefoni = set ()

        self.add_telefono(telefono)

        self.set_indirizzo(indirizzo)
    
    def set_nome(self, nome: str):

        self._nome = nome
    
    def telefoni(self) -> frozenset[str]:

        return frozenset(self._telefoni)
    
    def add_telefono(self, telefono: str):

        self._telefoni.add(telefono)
    

    def remove_telefono(self, t: str):

        if len(self.telefoni()) == 0:

            raise RuntimeError("il dipartimento deve avere almeno un numero di telefono")
        
        elif t not in self.telefoni():

            raise KeyError(f"non si può rimuovere il numero di telefono {t}")
        
        self._telefoni.remove(t)

        
         
    
    def indirizzo(self) -> Indirizzo:

        return self._indirizzo
    
    def set_indirizzo(self):

        pass



class Progetto:

    _nome: str

    _budget: RealGEZ
    
    







    
    