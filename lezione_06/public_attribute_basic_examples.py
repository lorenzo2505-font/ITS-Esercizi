class Animal:
    def __init__(self) -> None:
        self.name:str = "Generic Animal" # Public attribute


animal:Animal = Animal()

print(animal.name) # Output: "Generic Animal"

animal.name = "It's a dog" # MODIFIES the public attribute 'name'

print(animal.name) # Output: "It's a dog"

#they work.. but are extremely dangerous! 

