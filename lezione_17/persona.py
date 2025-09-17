class Persona:
    
    def __init__(self, first_name: str, last_name: str):
        
        if type(first_name) != str or type(last_name) != str:
            self.first_name = None
            
            raise ValueError('il nome o il cognome inserito non è una stringa')
        
        if type(first_name) != str and type(last_name) != str:
            self.età = 0
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
    
    def setName(self, first_name: str):
        
        if type(first_name) != str:
            raise ValueError('il nome inserito non è una stringa')
        
        self.first_name = first_name
    
    def setLastName(self, last_name: str):

        if type(last_name) != str:
            raise ValueError('il cognome inserito non è una stringa!')
        
        self.last_name = last_name
    
    def setAge(self, age: int):

        if type(age) != int:
            raise ValueError('il valore inserito non è un intero')
        
        self.age = age
    
    def getName(self) -> str:
        return self.first_name
    
    def getLastName(self) -> str:
        return self.last_name
    
    def getAge(self) -> int:
        return self.age
    
    def greet(self) -> None:
        print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni!")


if __name__ == '__main__':

    lorenzo: Persona = Persona('Lorenzo', 'Acomanni')
    lorenzo.setAge(20)
    lorenzo.greet()
    

    

    
