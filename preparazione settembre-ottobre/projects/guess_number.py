import random

def guess_number(minimo: int, massimo: int):

    tentativi = 0
    x: int = random.randint(minimo, massimo)

    for i in range(minimo, massimo + 1):

        y: int = int(input("indovina numero: "))
        tentativi += 1

        if x == y:
            print(f"indovinato!, {tentativi} tentavi su {massimo}, {tentativi}/{massimo}")
            break
        
        else:
            print("ritenta!")
    
    if tentativi == massimo:
        print(f"hai esaurito tutti i tentativi, {tentativi}/{massimo}")



def main():

    guess_number(1, 10)

main()


    
    
