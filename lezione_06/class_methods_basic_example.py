class Person:
    __population:int = 0 # Private class attribute
    def __init__(self, name:str) -> None:
        self.__name:str = name # Private attribute
        Person.__population += 1
    @classmethod
    def get_population(cls) -> None:
        return cls.__population
    
print(Person.get_population()) # Output: 0

person1:Person = Person("Alice")

print(Person.get_population()) # Output: 1

person2:Person = Person("Bob")

print(Person.get_population()) # Output: 2