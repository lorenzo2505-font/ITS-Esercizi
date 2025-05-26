from enum import *





from custom_types import *


    

class Studente:

    _matricola: int #<<imm>>, noto alla nascita

    _nome: str #noto alla nascita

    _genere: Genere #noto alla nascita

    _telefono: set [Telefono] #noto alla nascita [1..*]

    _email: set [Email] # non noto alla nascita [0..*]

    


    def matricola(self) ->int:

        return self._matricola
    
    def nome(self) -> str:

        return self._nome
    
    def genere(self) -> str:

        return self ._genere
    
    def telefono(self) -> frozenset:

        return frozenset(self._telefono)
    
    def email(self) -> frozenset:

        return frozenset(self._email)
    
    def set_nome(self, nome: str):

        self._nome = nome

    def set_genere(self, genere: str):

        self._genere = genere
    
    def add_telefono(self, t):

        self._telefono.add(t)
    
    def remove_telefono(self, t):

        if len(self.telefono()) > 1:
            self._telefono.remove(t)
        
        raise RuntimeError("uno studente...")
    