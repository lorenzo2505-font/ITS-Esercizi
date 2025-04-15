class Persona:
    def __init__ (self, name: str, lastname: str, age: int):
        self.setName(name) 
        self.setLastName(lastname)
        self.setAge(age)

    def setName (self, name: str) -> None:
        if name:

            self.name = name
        else:
            print("errore")

    def setLastName (self, lastname: str) -> None:
        if lastname:

            self.lastname = lastname
        else:
            print("errore")

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
    
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    def __call__(self):
        if self.age < 18:
            print(f"{self.name} {self.lastname} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.lastname} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.lastname} e' una persona adulta!")
        else:
            print(f"{self.name} {self.lastname} e' una persona anziana!")