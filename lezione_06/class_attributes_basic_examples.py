class Person:
    population:int = 0 # Public class attribute
    def __init__(self, name:str) -> None:
        self.__name:str = name # Private attribute
        Person.population += 1


print(Person.population) # Output: 0

person1:Person = Person("Alice")

print(Person.population) # Output: 1

person2:Person = Person("Bob")

print(Person.population) # Output: 2