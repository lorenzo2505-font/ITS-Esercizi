class Animal: #base class
    def speak(self) -> None:
        print("The animal makes a sound")

class Dog(Animal): #derived class
    def bark(self) -> None:
        print("Woof!")

fido:Dog = Dog()

fido.speak() # Output: "The animal makes a sound"

fido.bark() # Output: "Woof!"

