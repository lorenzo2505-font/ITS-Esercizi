'''1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether 
    the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''




def school_grading_system(student: str, grades: list[int]):

    av = sum(grades) / len(grades)

    if av >= 60:

        print(f"the student: {student}, passed the exam, average: {av}")
    
    else:
        print(f"the student: {student}, did not pass the exam, average: {av}")

    



mylist: list [dict] = [{"lorenzo": [60, 70, 80]}, {"saud": [30, 40, 50]}]

for i in range(len(mylist)):

    for key, value in mylist[i].items():

        school_grading_system(key, value)




    











    



        


