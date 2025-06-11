
# gestione dei link di associazione 


from typing import Any


from voli_aerei3 import *



class volo_comp:

    '''gli oggetti di questa classe rappresentano link di associazione volo-comp'''

    _volo: Volo

    _compagnia: Compagnia


    def __init__(self, v: Volo, c: Compagnia):

        self._volo = v

        self._compagnia = c
    
    def volo(self) -> Volo:

        return self._volo
    
    def compagnia(self) -> Compagnia:

        return self._compagnia
    
    def __hash__(self) -> int:
        

        return hash((self._volo, self._compagnia))
    
    def __eq__(self, other: Any) -> bool:

        
        if type(self) != type(other) or hash(self) != hash(other):

            return False
        
        return self.volo() is other.volo() and self.compagnia() is other.compagnia()
    




# responsabilità singola


class Studente:

    _nome: str

    def __init__(self, nome: str) -> None:

        self.setNome(nome)
    
    def nome(self):

        return self._nome
    
    def setNome(self, nome: str):

        self._nome = nome




class Modulo:
    pass











class Esame:

    _studente: Studente

    _modulo: Modulo
    


        