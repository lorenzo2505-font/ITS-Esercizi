'''1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too. '''

class Student:
    def __init__ (self, name: str, study_program: str, age: int, gender: str):
        self.name = name
        self.study_program = study_program
        self.age = age
        self.gender = gender
    
    def print_info (self):
        print(f"{self.name}, {self.study_program}, {self.age}, {self.gender}")


lorenzo = Student  ("Lorenzo Acomanni", "Python", 19, "M")
luca = Student ("Luca D'Ambra", "Progettazione", 21,  "M")
camilla = Student ("Camilla Provenzano", "Sistemi Digitali", 24,  "F")

lorenzo.print_info()
luca.print_info()
camilla.print_info()