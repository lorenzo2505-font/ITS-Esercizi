# Without super()

'''class Animal:
    def __init__(self, name:str) -> None:
        self.name:str = name
        print("Animal initialized")

class Dog(Animal):
    def __init__(self, name:str) -> None:
        self.name:str = name
        print("Dog initialized")

fido:Dog = Dog("Rudy")
# Output: Dog initialized'''


# With super()
class Animal:
    def __init__(self, name:str) -> None:
        self.name:str = name    
        print("Animal initialized")

class Dog(Animal):
    def __init__(self, name:str) -> None:
        super().__init__(name) #parent class __init__() 
        print("Dog initialized")

fido:Dog = Dog("Rudy")
# Output: Animal initialized
# Dog initialized