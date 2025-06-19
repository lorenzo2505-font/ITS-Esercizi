from __future__ import annotations


from custom_types import *


from datetime import date



class Impiegato:
    _nome: str # noto alla nascita

    _cognome: str # noto alla nascita

    _nascita: date # <<immutable>>, # noto alla nascita

    _stipendio: RealGEZ # # noto alla nascita

    _progetti: dict [Progetto, coinvolto._link]

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: RealGEZ) -> None:
        self.set_nome(nome)

        self.set_cognome(cognome)

        self._nascita = nascita

        self.set_stipendio(stipendio)

        self._progetti = dict()
    

    '''def progetti(self) -> frozenset[_coinvolto]:

        return frozenset(self._progetti.values())
    
    def progetto(self, progetto: Progetto) -> _coinvolto:

        return self._progetti[progetto]
    
    def add_progetto(self, progetto: Progetto, data: date):

        if progetto in self._progetti:

            raise KeyError(f"l'impiegato: {self.nome()} fa già parte del progetto")
        
        c: _coinvolto = _coinvolto(self, progetto, data)

        self._progetti[progetto] = c
    
    def remove_progetto(self, progetto: Progetto) -> None:

        if progetto not in self._progetti:

            raise KeyError(f"l'impiegato: {self.nome()} non è mai stato coinvolto nel progetto")
        
        del self._progetti[progetto]'''
    




    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio
    

    def _add_link_coinvolto(self, l: coinvolto._link):


        if l.impiegato() != self:

            raise ValueError(f"il link non coinvolge me ma un'altro impiegato")

        if l.progetto() in self._progetti:

            raise KeyError(f"l'impiegato {self.nome()} è già coinvolto nel progetto")
        
        
        

        self._progetti[l.progetto()] = l

    def progetti(self) -> frozenset["coinvolto._link"]:

        return frozenset(self._progetti.values())
    
    def is_coinvolto(self, progetto: "Progetto") -> bool:

        return progetto in self._progetti
    
    def data_coinvolgimento(self, progetto: "Progetto") -> date:

        if progetto not in self._progetti:

            raise ValueError("l'impiegato non è coinvolto nel progetto")
        
        return self._progetti[progetto].data()

    def __str__(self) -> str:
        return (f"{self.nome()} {self.cognome()}, "
                f"nascita: {self.nascita()}, "
                f"stipendio: {self.stipendio()}")


    



class Citta:
    _nome: str

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome












class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[str] # [1..*] (e quindi noto alla nascita)
    _indirizzo: Indirizzo # mutabile, [0..1], certamente noto alla nascita
    _citta: Citta # noto alla nascita

    def __init__(self, nome: str, telefono: str, indirizzo: Indirizzo,
                 c: Citta) -> None:
        self.set_nome(nome)

        self._telefoni = set()
        self.add_telefono(telefono)

        self.set_indirizzo(indirizzo)
        self.set_citta(c)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def telefoni(self) -> frozenset[str]:
        return frozenset(self._telefoni)
    
    def add_telefono(self, telefono: str) -> None:
        self._telefoni.add(telefono)

    def remove_telefono(self, t: str) -> None:
        if len(self.telefoni()) == 1:
            raise RuntimeError('Il dipartimento deve avere almeno un numero di telefono')
        elif t not in self.telefoni():
            raise KeyError(f"Non posso rimuovere il numero di telefono {t} che non appartiene al dipartimento")

        self._telefoni.remove(t)

    def indirizzo(self) -> Indirizzo:
        return self._indirizzo
    
    def set_indirizzo(self, indirizzo: Indirizzo|None) -> None:
        self._indirizzo = indirizzo

    def remove_indirizzo(self) -> None:
        self.set_indirizzo(None)

    def citta(self) -> Citta:
        return self._citta

    def set_citta(self, c: Citta) -> None:
        self._citta = c



    def __repr__(self) -> str:
        return f'Dipartimento({self._nome}, {self._telefoni}, {self._indirizzo}, {self._citta})'

    def __str__(self) -> str:
        if self.indirizzo():
            ind_str: str = "con sede in " + str(self.indirizzo())
        else:
            ind_str: str = "senza sede"

        tel_str: str = "[" + ", ".join(self.telefoni()) + "]"

        return f"Dipartimento '{self.nome()}' {ind_str} a {self.citta()} e numeri di telefono: {tel_str}"
    










class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita

    _impiegati: dict [Impiegato, coinvolto._link]

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self._nome = nome
        self._budget = budget

    def nome(self) -> str:
        return self._nome

    def budget(self) -> RealGEZ:
        return self._budget

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGEZ:
        return self._budget
    
    def _add_link_coinvolto(self, l: coinvolto._link):


        if l.progetto() != self:

            raise ValueError("il link non coinvolge me")
        
        if l.impiegato() in self._impiegati:

            raise KeyError("l'impiegato: è già coinvolto nel progetto")

        self._impiegati[l.impiegato()] = l

    def __str__(self) -> str:
        return f"Progetto '{self.nome()}' con budget: {self.budget()}€"

    def __repr__(self) -> str:
        return f"Progetto(nome={self.get_nome()}, budget={self.budget()})"



class coinvolto:

    @staticmethod

    def add(cls, progetto: Progetto, impiegato: Impiegato, data: date):

        l = cls._link(progetto, impiegato, data)

        progetto._add_link_coinvolto(l)

        impiegato._add_link_coinvolto(l)
    
    @staticmethod

    def remove(cls, l: _link):

        l.progetto()._remove_link_coinvolto(l)

        l.impiegato()._remove_link_coinvolto(l)
        

        del l

    class _link:

        _impiegato: Impiegato

        _progetto: Progetto

        _data: date # <<imm>, noto alla nascita

        def __init__(self, impiegato: Impiegato, progetto: Progetto, data: date):

            self._impiegato = impiegato

            self._progetto = progetto

            self._data = data
        
        def impiegato (self):

            return self._impiegato
        
        def progetto(self):

            return self._progetto
        
        def data(self):

            return self._data
        
        def __hash__(self) -> int:

            return hash((self._impiegato, self._progetto))
        
        def __eq__(self, other: Any) -> bool:

            if type(self) != type(other) or hash(self) != hash(other):

                return False
            
            return self.impiegato() is other.impiegato() and self.progetto() is other.progetto()
        

        def __repr__(self):
            
            return f"{self.impiegato()} è stato convilto a: {self.data()} in {self.progetto()}"
        

