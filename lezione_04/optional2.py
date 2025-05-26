'''2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.

    Prompt the user to guess the number within a specified maximum number of attempts.

    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.

    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.


'''


import random 

def guess_the_number_game (n1: int, n2: int):

    n3 = random.randint(n1, n2)

    attemps = 3

    for i in range(attemps):

        g: int = int(input("which is the number ?: "))

        if g == n3:

            print("correct!")
            break
        
        elif g > n3:

            print("wrong!, too high!")
        
        else:

            print("wrong!, too low!")


guess_the_number_game(1, 10)
        
        




        

