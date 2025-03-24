'''Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal'''

class Animal:
    def __init__ (self, name: str, legs: int):
        self.name = name
        self.legs = legs

    def set_legs (self, legs: int):
        self.legs = legs
    
    def get_legs (self):
        return self.legs
    
    def print_info (self):
        print(f"{self.name}, {self.legs}")

    
        

tiger = Animal ("Tiger", 4)
python = Animal ("Python", 0)

print(tiger.name)
print(python.name)

spider = Animal("Spider", 8)

spider.set_legs (8)

print(spider.get_legs())

wolf = Animal ("Wolf", 4)

wolf.print_info()








