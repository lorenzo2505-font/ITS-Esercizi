from __future__ import annotations

from custom_types import *




class Nazione:

    _nome: str # noto alla nascita

    def __init__(self, nome: str):
        
        self.setNome(nome)
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            ValueError("inserire un nome valido")
    

    def nome(self):

        return self._nome
    
    def __str__(self):
        
        return f"nome nazione: {self._nome}"













class Città:

    _nome: str # noto alla nascita

    _abitanti: int # noto alla nascita

    _nazione: Nazione # noto alla nascita


    def __init__(self, nome: str, abitanti: int, nazione: Nazione):
        


        self.setNome(nome)

        self.setAbitanti(abitanti)

        self.setNazione(nazione)
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    
    def setAbitanti(self, abitanti: int):

        if abitanti >= 0:

            self._abitanti = abitanti
        
        else:

            raise ValueError("il numero di abitanti non può essere negativo")
    
    def setNazione(self, nazione: Nazione):

        self._nazione = nazione
    

    def nome(self):

        return self._nome
    
    def abitanti(self):

        return self._abitanti
    
    def nazione(self):

        return self._nazione
    
    def __str__(self):
        
        return f"nome città: {self._nome}, abitanti: {self._abitanti}"











class Aereoporto:

    _nome: str # noto alla nascita

    _codice: CodiceAereoporto # <<immutable>> noto alla nascita

    _città: Città # <<immutable>> noto alla nascita 


    def __init__(self, nome: str, codice: CodiceAereoporto, città: Città):
        
        self.setNome(nome)

        self._codice = codice

        self._città = città
    

    def setNome(self, nome: str):

        
        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    

    def nome(self):

        return self._nome
    
    def codice(self):

        return self._codice
    
    def città (self):

        return self._città
    
    def __str__(self):

        return f"nome aereoporto: {self._nome}, codice: {self._codice}"
    
    





    












class Compagnia:

    _nome: str # noto alla nascita 

    _anno: int # <<immutable>> noto alla nascita

    _città: Città # noto alla nascita

    _voli: set [Volo]

    
    def __init__(self, nome: str, anno: int, città: Città):
        
        self.setNome(nome)

        if anno > 1900:

            self._anno = anno
        
        else:

            ValueError ("inserire un anno di fondazione prima del 1900")
        
        self.setCittà(città)

        self._voli = set()

        
    

    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            ValueError("inserire un nome valido")
    
    def setCittà(self, città: Città):

        self._città = città
    
    def add_voli(self, volo: Volo):

        self._voli.add(volo)
    
    def remove_voli(self, volo: Volo):

        self._voli.remove(volo)
    
    def nome(self):

        return self._nome
    
    def anno(self):

        return self._anno
    
    def città(self):

        return self._città
    
    def voli(self) -> frozenset[Volo]:

        return frozenset[self._voli]
    
    def __str__(self):
        
        return f"nome compagnia: {self._nome}, anno di fondazione: {self._anno}"




















class Volo:

    _durata_min: int # noto alla nascita

    _codice: CodiceVolo # <<immutable>>, noto alla nascita

    _compagnia: Compagnia # <<immutable>>, noto alla nascita

    _aereoportoPartenza: Aereoporto # <<immutable>>, noto alla nascita

    _aereportoArrivo: Aereoporto # noto alla nascita


    


    def __init__(self, durata_min: int, codice: CodiceVolo, compagnia: Compagnia, aereoportoPartenza: Aereoporto, aereoportoArrivo: Aereoporto):
        

        self.setDurata(durata_min)

        self._codice = codice

        self._compagnia = compagnia

        self._aereoportoPartenza = aereoportoPartenza

        self.setAereoportoArrivo(aereoportoArrivo)

        compagnia.add_voli(self)
    
    def setDurata(self, durata_min: int):

        if durata_min <= 0:

            raise ValueError("non ci possono essere durate di voli con valore minore o uguale a zero")
        
        else:

            self._durata = durata_min
    
    def setAereoportoArrivo(self, aereportoArrivo: Aereoporto):

        self._aereportoArrivo = aereportoArrivo
    
    def durata(self):

        return self._durata
    
    def codice(self):

        return self._codice
    
    def compagnia(self):

        return self._compagnia
    
    def aereoportoPartenza(self):

        return self._aereoportoPartenza
    
    def aereoportoArrivo(self):

        return self._aereportoArrivo
    
    
    def __str__(self):
        
        return f"durata volo: {self._durata} minuti, codice: {self._codice}"





'''n: Nazione = Nazione("italia")

print(n)


c: Città = Città("roma", 3000000, n)

print(c)


cod1: CodiceAereoporto = CodiceAereoporto("FCO")

a: Aereoporto = Aereoporto("aereporto di fiumicino", cod1 , c)

print(a)


comp: Compagnia = Compagnia("pierlions company", 1998, c)

print(comp)


cod2: CodiceVolo = CodiceVolo("AZ123")

cod3: CodiceAereoporto = CodiceAereoporto("MLO")

milano: Città = Città("milano", 2000000, n)

aArrivo: Aereoporto = Aereoporto ("aereporto di milano", cod3, milano)


v: Volo = Volo (60, cod2, comp, a, aArrivo)

print(v)'''






    

















        





        
