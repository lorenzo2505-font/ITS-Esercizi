'''class Person:
 
 personCount = 0

 def __init__(self, name):
    self.name = name
    personCount += 1

alice = Person("Alice W.")
bob = Person("Bob M.")
print(Person.personCount)'''

class Student:
    studentGrades = []

    def __init__(self, studentName, grade):
        self.name = studentName
        self.studentGrades.append(grade)

    def getGroupAverage(cls):
        avg = sum(cls.studentGrades) / len(cls.studentGrades)
        return avg

print("hello")