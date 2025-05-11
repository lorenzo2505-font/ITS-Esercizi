'''1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''



def school_grading_system (name: str):


    materie: list = ["italiano", "matematica", "filosofia", "fisica", "scienze", "inglese", "storia", "informatica"]

    voti: list[float] = []

    for i in range(len(materie)):

        voto: float = float(input(f"inserisci la media di {materie[i]}: "))

        voti.append(voto)

    return f"la media di {name} è {sum(voti) / len(materie)}"


s = school_grading_system ("lorenzo")

print(s)

    



        


