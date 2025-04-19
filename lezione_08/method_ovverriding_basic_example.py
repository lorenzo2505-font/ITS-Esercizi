class Animal:
    def speak(self) -> None:
        print("The animal makes a sound")

class Cat(Animal):
    def speak(self) -> None:
        print("Meow!")

kitty:Cat = Cat()
kitty.speak() # Output: "Meow!"

