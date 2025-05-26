from enum import *

#from typing import Self

from typing import Any

import time

from datetime import date

import re













class Persona:

    def __init__(self, nome: str, cognome: str,  data_nascita: date, codice_fiscale: str):

        self.set_nome(nome)

        self.set_cognome(cognome)

        self.set_data(data_nascita)

        self.set_cf(codice_fiscale)

        
    
    def set_nome(self, nome: str):

        if nome:

            self.nome = nome
        
        else:

            raise Exception("inserire un nome valido")
    
    def set_cognome(self, cognome: str):

        if cognome:

            self.cognome = cognome
        
        else:

            raise Exception("inserire un cognome valido")
    
    def set_data(self, data_nascita: date):

        self.data = data_nascita

    
    def set_cf(self, codice_fiscale: str):

        pattern = r"^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$"

        if not re.match(pattern, codice_fiscale):

            raise Exception("il codice fiscale deve rispettare lo specifico modello, non può essere diverso")
        else:
            self.cf = codice_fiscale
    
    def get_nome(self):

        return self.nome
    
    def get_cognome(self):

        return self.cognome
    
    def get_data(self):

        return self.data
    
    def get_cf(self):

        return self.cf
    
    def __hash__(self):
        
        return hash(self.cf())
    
    def __eq__(self, other: Any):

        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return (self.cf()) == (other.cf())

     
    
    def __str__(self):

        return f"nome: {self.nome}, cognome: {self.cognome}, data di nascita: {self.data}, codice fiscale: {self.cf}"
    



class PosM (Enum):


    assolto = auto ()

    esente = auto()

    dispensato = auto()



    
        
    
    
    



class Uomo(Persona):


    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, posizione_militare: PosM):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)

        self.set_pos_m(posizione_militare)
    
    def set_pos_m(self, posizione_militare: PosM):

        if posizione_militare:

            self.pos_m = posizione_militare
        
        else:

            raise Exception("deve essere inserita una posizione valida")
    
    def get_pos_m(self):

        return self.pos_m
    
    
    def __str__(self):
        return super().__str__() + f", posizione militare: {self.pos_m}"



'''l: Uomo = Uomo("lorenzo", "acomanni", date(2005, 3, 25), "ABCDEF05G25H501I", PosM.esente)


print(l)'''



class Donna (Persona):

    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, maternità: int):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)

        self.set_maternità(maternità)

    def set_maternità(self, maternità: int):

        if maternità < 0:

            raise Exception("la maternità non può avere un valore minore di zero")
        
        else:

            self.maternità = maternità
    
    def get_maternità(self):

        return self.maternità
    
    def __str__(self):
        return super().__str__() + f", numero di maternità: {self.maternità}"


'''r: Donna = Donna("roberta", "cirillo", date(1974, 7, 14), "ABCDEF05G25H501I", 2)

print(r)'''


class Studente (Persona):

    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, matricola: int):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)

        self.set_matricola(matricola)
    
    def set_matricola(self, matricola: int):

        if (len(str(matricola)) < 8) or (len(str(matricola)) > 8):

            raise Exception("la matricola deve essere composta da 8 cifre")
        
        else:

            self.matricola = matricola
    

    def get_matricola(self):

        return self.matricola
    
    def __hash__(self):

        return hash(self.cf(), self.matricola())


        
    
    def __eq__(self, other: Any):

        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return (self.cf(), self.matricola()) == (other.cf(), other.matricola())
    
    def __str__(self):
        return super().__str__() + f", matricola: {self.matricola}"





class Impiegato (Persona):

    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)

        self.set_stipendio(stipendio)

    
    def set_stipendio(self, stipendio: float):

        if stipendio < 0.0:

            raise Exception("lo stipendio non può avere un valore negativo")
        
        else:

            self.stipendio = stipendio
    
    def get_stipendio(self):

        return self.stipendio
    
    def __str__(self):
        return super().__str__() + f", stipendio {self.stipendio} euro"
    

class Segretario (Impiegato):

    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, stipendio)
    
    def __str__(self):
        return super().__str__() + ", ruolo: Segretario"


class Direttore (Impiegato):

    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, stipendio)
    
    def __str__(self):
        return super().__str__() + ", ruolo: Direttore"


class Progettista (Impiegato):

    def __init__(self, nome: str, cognome: str, data_nascita: date, codice_fiscale: str, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, stipendio)
    
    def __str__(self):
        return super().__str__() + ", ruolo: Progettista"


class Progetto:

    def __init__(self, nome: str, progettisti: list[Progettista]):
        
        self.set_nome(nome)

        self.set_progettisti(progettisti)
    
    def set_nome(self, nome: str):

        if nome:

            self.nome = nome
        
        else:

            raise Exception("inserire un nome valido")
    
    def set_progettisti(self, progettisti: list[Progettista]):

        if progettisti:

            self.progettisti = progettisti
        
        else:

            raise Exception("inserire un elenco valido")
    
    def get_nome(self):

        return self.nome
    
    def get_progettisti(self):

        return self.progettisti

    def __str__(self):

        return f"nome progetto: {self.nome}, progettisti coinvolti: {self.progettisti}"

        

            



    

        


    


    
    

        
    



        