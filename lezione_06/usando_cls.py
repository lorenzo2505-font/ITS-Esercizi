class Student:
    studentGrades = []

    def __init__(self, studentName, grade):
        self.name = studentName
        self.studentGrades.append(grade)

    def getGroupAverage(cls):
        avg = sum(cls.studentGrades) / len(cls.studentGrades)
    
        return avg