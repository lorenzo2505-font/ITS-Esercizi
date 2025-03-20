class Persona:
    def __init__ (self):
        self.name = "" 
        self.lastname = ""
        self.age = 0

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")
    #mi consente di impostare un valore per self.name
    def setName (self, name: str) -> None:
        self.name = name
    def setLastName (self, lastname: str) -> None:
        self.lastname = lastname
    def setAge (self, age) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = 0
    #ritorna il valore di name
    def getName (self) -> str:
        return self.name
    #ritorna il valore di lastname
    def getLastName (self) -> str:
        return self.lastname
    def getAge (self) -> int:
        return self.age

#crea un oggetto di tipo persona 
la: Persona = Persona ()

#stampa i dati della persona creata
la.displayData ()

#impostare il nome di una persona 
la.setName ("Lorenzo")

#impostare il cognome di una persona
la.setLastName ("Acomanni")

#impostare l'età di una persona 
la.setAge(19)


print(la.getName(), la.getLastName (), la.setAge ())





        