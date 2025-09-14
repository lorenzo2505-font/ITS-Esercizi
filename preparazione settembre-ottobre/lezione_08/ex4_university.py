from __future__ import annotations
from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self, nome: str, età: int):
        super().__init__()

        self.nome = nome
        self.età = età
    
    @abstractmethod

    def get_role():
        pass

    def __str__(self):
        return super().__str__() + f"nome: {self.nome}, età: {self.età}"

class Studente(Persona):

    def __init__(self, nome: str, età: int, id: int):
        super().__init__(nome, età)

        self.id = id
        self.corsi: list[Corso] = []
    
    def enroll(self, corso: Corso):
        
        if corso in self.corsi:

            raise ValueError("lo studente è già iscritto a questo corso")
        
        self.corsi.append(corso)
    
    def get_role(self):
        
        return type(self)
    


class Professore(Persona):
    
    def __init__(self, nome: str, età: int, id: int):
        super().__init__(nome, età)

        self.id = id
        self.dipartimento: Dipartimento = ""
        self.corsi: list[Corso] = []
    
    def assign_to_course(self, corso: Corso):
        
        if corso in self.corsi:

            raise ValueError("questo corso è già stato assegnato al professore")
        
        self.corsi.append(corso)
    
    def set_department(self, dipartimento: Dipartimento):

        self.dipartimento = dipartimento
    
    def get_role(self):
        
        return type(self)


class Corso:
    
    def __init__(self, nome: str, codice: int):
        
        self.nome = nome
        self.codice = codice
        self.professore: Professore = ""
        self.studenti: list[Studente] = []
        
        

    def add_student(self, studente: Studente):

        if studente in self.studenti:

            raise ValueError("lo studente fa già parte di questo corso")

        if self not in studente.corsi:

            raise ValueError("lo studente non si è iscritto a questo corso")

        self.studenti.append(studente) 
    
    def set_professor(self, professore: Professore):

        if self not in professore.corsi:

            raise ValueError("al professore non è stato assegnato questo corso")
        
        self.professore = professore
    
    def __str__(self):
        
        return f"nome corso: {self.nome}, codice: {self.codice}, professore: {self.professore}, studenti: {self.__repr__()}"
    
    def __repr__(self):
        
        return f"{self.studenti}"
    


class Dipartimento:
    
    def __init__(self, nome: str):

        self.nome = nome
        self.corsi: list[Corso] = []
        self.professori: list[Professore] = []
    
    def add_course(self, corso: Corso):

        if corso in self.corsi:

            raise ValueError("il corso è già presente nell'elenco")
        
        self.corsi.append(corso)
    
    def add_professor(self, professore: Professore):

        if professore.dipartimento == self:
            
            self.professori.append(professore)
        
        else:

            raise ValueError("a quasto professore non è stato assegnato il nostro dipartimento")
    
    def __str__(self):
        
        return f"nome dipartimento: {self.nome}, professori: {self.__repr__()}"
    
    def __repr__(self):
        
        return f"{self.professori}"


class Università:

    def __init__(self, nome: str):

        self.nome = nome
        self.dipartimenti: list[Dipartimento] = []
        self.studenti: list[Studente] = []
    
    def add_department(self, dipartimento: Dipartimento):

        if dipartimento in self.dipartimenti:
            
            raise ValueError("questo dipartimento è già stato aggiunto")
        
        self.dipartimenti.append(dipartimento)
    
    def add_student(self, studente: Studente):

        if studente in self.studenti:

            raise ValueError("lo studente è già iscritto all'università")
        
        self.studenti.append(studente)
    
    def __str__(self):

        return f"nome università: {self.nome}, {self.__repr__()}"
    
    def __repr__(self):
        
        return f"dipartimenti: {self.dipartimenti}, studenti: {self.studenti}"



def main():

    sapienza: Università = Università("sapienza")
    
    dip_informatica: Dipartimento = Dipartimento("informatica")

    basi_di_dati: Corso = Corso("basi di dati", 3)

    esposito: Professore = Professore("marco esposito", 31, 1)

    popa: Studente = Studente("alessandro popa", 21, 2)

    sapienza.add_department(dip_informatica)
    sapienza.add_student(popa)

    popa.enroll(basi_di_dati)
    basi_di_dati.add_student(popa)

    esposito.assign_to_course(basi_di_dati)
    basi_di_dati.set_professor(esposito)

    print(sapienza)
    print(dip_informatica)
    print(basi_di_dati)
    print(esposito)
    print(popa)



main()







        
        

    
