class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    

alice = Person ("Alice", 45)

bob = Person ("Bob", 30)

#print(alice.age)

print(bob.age)

if alice.age > bob.age:
    print(alice.age)
elif bob.age > alice.age:
    print(bob.age)
else:
    pass

matteo = Person ("Matteo", 21)
camilla = Person ("Camilla", 24)
thomas = Person ("Thomas", 19)

people = [alice, bob, matteo, camilla, thomas]



minimo = 9999999999
minimo_nome = None

for i in people:
    if i.age < minimo:
        minimo = i.age
        minimo_nome = i.name
print(minimo_nome)






    

    

