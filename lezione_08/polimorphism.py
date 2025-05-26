class Animal:
    def speak(self) -> None:
        print("Generic sound")
    

class Dog(Animal):
    def speak(self) -> None:
        print("Woof!")

class Cat(Animal):
    def speak(self) -> None:
        print("Meow!")

def make_speak(animal: Animal) -> None:
        animal.speak()


make_speak(Cat()) # Output "Meow!"
make_speak(Dog()) # Output "Woof!"



