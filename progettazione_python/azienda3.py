from custom_types import *


from datetime import date


class Impiegato:


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ):

        self.set_nome(nome)

        self.set_cognome(cognome)

        self._nascita = nascita

        self.set_stipendio(stipendio)

    
    def set_nome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome adatto")
    
    def set_cognome(self, cognome: str):

        if cognome:

            self._cognome = cognome
        
        else: 

            raise ValueError("inserire un cognome adatto")

    

    def set_stipendio(self, stipendio: RealGEZ):

        self._stipendio = stipendio
    

    def get_nome(self):

        return self._nome
    
    def get_cognome(self):

        return self._cognome
    
    def get_nascita(self):

        return self._nascita
    
    def get_stipendio(self):

        return self._stipendio
    
    def __str__(self):
        
        return f"nome impiegato: {self._nome}, cognome: {self._cognome}, nascita: {self._nascita}, stipendio: {self._stipendio} euro"
    

i: Impiegato = Impiegato("lorenzo", "acomanni", date(day = 25, month = 3, year = 2005), 5.0)

#print(i)





class Dipartimento:

    def __init__(self, nome: str, telefono: set[Telefono], indirizzo: Indirizzo):


        self.set_nome(nome)

        self.set_telefono(telefono)

        self.set_indirizzo(indirizzo)

    
    def set_nome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    
    def set_telefono(self, telefono: set[Telefono]):

        self._telefono = telefono
    
    def set_indirizzo(self, indirizzo: Indirizzo):

        self._indirizzo = indirizzo
    
    def get_nome(self):

        return self._nome
    
    def get_telefono(self) -> frozenset[Telefono]:

        return self._telefono
    
    def get_indirizzo(self):

        return self._indirizzo
    
    def __str__(self):

        return f"nome del dipartimento: {self._nome}, telefoni disponibili: {self._telefono}, indirizzo: {self._indirizzo}"



d: Dipartimento = Dipartimento("DIP01", (Telefono("3928451155")), Indirizzo("viale cesare pavese", 305))


#print(d)



class Progetto:

    def __init__(self, nome: str, budget: RealGEZ):


        self.set_nome(nome)

        self.set_budget(budget)
    
    def set_nome(self, nome: str):

        if nome:

            self._nome = nome

        else:

            raise ValueError("inserire un nome valido")
    
    def set_budget(self, budget: RealGEZ):

        self._budget = budget
    
    def get_nome(self):

        return self._nome
    
    def get_budget(self):

        return self._budget
    
    def __str__(self):
        
        return f"nome del progetto: {self._nome}, budget: {self._budget} euro"
    
p: Progetto = Progetto ("project blue lock", 500000000.0)

print(p)

            
    
    

        

        
        



