from typing import Any
'''ask the users a bunch of and then,
if they give us the right answer to these question
we'll kind of add one to their score,
at the end of the program we'll print out what they got out of,
the number of question they got'''

def quiz_game():

    punteggio = 0
    print("inizia il questionario")

    print("domanda 1: Qual è la capitale della Francia?")
    dict1: dict = {"A": "Londra", "B": "Madrid", "C": "Parigi", "D": "Roma"}

    for key, value in dict1.items():
        print(f"{key}: {value}")
    
    risposta1 = input("risposta: ")
    
    if risposta1 not in dict1:
        
        raise ValueError("la risposta che hai messo non è tra le possibili del dizionario")
    
    elif risposta1 == "C":
        punteggio += 1
    
    print("domanda 2: Quanti continenti ci sono sulla Terra?")
    dict2: dict = {"A": 5, "B": 6, "C": 7, "D": 8}

    for key, value in dict2.items():
        print(f"{key}: {value}")
    
       
    risposta2 = input("risposta: ")
    
    if risposta2 not in dict2:
        
        raise ValueError("la risposta che hai messo non è tra le possibili del questionario")
    
    elif risposta2 == "C":
        punteggio += 1
    
    print("domanda 3: Chi ha scritto Amleto?")
    dict3: dict = {"A": "Charles Dickens", "B":  "William Shakespeare", "C": "Mark Twain", "D": "Oscar Wilde"}

    for key, value in dict3.items():
        print(f"{key}: {value}")
    
       
    risposta3 = input("risposta: ")
    
    if risposta3 not in dict3:
        
        raise ValueError("la risposta che hai messo non è tra le possibili del questionario")
    
    elif risposta3 == "B":
        punteggio += 1
    
    print(f"punteggio: {punteggio}/3")


#quiz_game()

    



def pseudo(mylist: list[dict[str, dict]], giuste: list[str]):

    if len(mylist) != len(giuste):

        raise ValueError("le due liste non combaciano di lunghezza")
    
    '''for i in range(len(mylist)):
        
        if giuste[i] not in mylist[i].values():

            raise ValueError("questa risposta non è tra le possibili del questionario")'''

    punteggio = 0

    for i in range(len(mylist)):

        for domanda, risposte in mylist[i].items():
            print(domanda)

            for key, value in risposte.items():
                print(f"{key}: {value}")
            
            risposta = input("risposta: ")

            if risposta not in risposte:

                raise ValueError("la risposta che hai messo non è tra le possibili del questionario")
            
            elif risposta == giuste[i]:
                punteggio += 1
    
    print(f"punteggio: {punteggio}/{len(mylist)}")


dict1: dict = {"A": "Londra", "B": "Madrid", "C": "Parigi", "D": "Roma"}
dict2: dict = {"A": 5, "B": 6, "C": 7, "D": 8}
dict3: dict = {"A": "Charles Dickens", "B":  "William Shakespeare", "C": "Mark Twain", "D": "Oscar Wilde"}

lista: list[dict[str, dict]] = [
    {"domanda 1: Qual è la capitale della Francia?": dict1},
    {"domanda 2: Quanti continenti ci sono sulla Terra?": dict2},
    {"domanda 3: Chi ha scritto Amleto?": dict3}

]

check: list[str] = ["C", "C", "B"]

pseudo(lista, check)








    

    

