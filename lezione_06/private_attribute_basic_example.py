class Animal:
    def __init__(self) -> None:
        self.__name:str = "Generic Animal" # Private attribute

# Makes 'name' accessible again
    def get_name(self) -> str:
        return self.__name
    
    
animal:Animal = Animal()
print(animal.get_name()) # Output: "Generic Animal"