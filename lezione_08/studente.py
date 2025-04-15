#importare dal modulo lezione_eridarietà.py la classe Persona

from lezione_ereditarietà import Persona

class Studente(Persona):
    '''
    Attributi della classe Persona 

    self.name: str
    self.lastname: str
    self.age: int

    Attributi della classe Studente
    self.matricola: str

    '''

    #inizializzare un oggetto della classe studente

    def __init__ (self, name: str, lastname: str, age: int, matricola: str):




        #inizializzare la classe Persona richiamando il metodo init della superclasse
        super().__init__(name, lastname, age)

        #istruzioni che inizializzano un oggetto della classe Studente 

        self.set(matricola)


        #metodi setter 

        #metodo che imposta il valore dell'attributo self.matricola

    def setMatricola(self, matricola: str):
        if matricola:
            self.matricola = matricola
        else:
            print("errore")
    
    def getMatricola (self) ->str:
        return self.matricola
    
    #il metodo __str__

    def __str__(self) -> str:
        
        return f"Nome: {self.name}, Cognome: {self.lastname}, Matricola: {self.matricola}"


