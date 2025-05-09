class Person:
 
 def __init__(self, name, age):
    self.name = name
    self.age = age

 def printData(self):
    print(f"{self.name}: {self.age}")

alice = Person("Alice W.", 45)
alice.printData() 