class Animal:
    def __init__(self) -> None:
        self._type:str = "Mammal" # Protected attribute

    def _sound(self) -> None: # Protected method
        print("Generic animal sound")

class Dog(Animal):
    def describe(self) -> None:
        print(f"I am a {self._type}") # Accessing protected attribute
        self._sound() # Calling protected method

        
fido:Dog = Dog()
fido.describe() # Output: "I am a Mammal"
# Generic animal sound