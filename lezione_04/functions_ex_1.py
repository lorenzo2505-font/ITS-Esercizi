'''Scrivi una funzione check_value(), che accetta un numero come argomento.
Utilizzando if / else, la funzione dovrebbe stampare se il numero è maggiore, minore o uguale a 5.
'''


def check_value(num: int):
    if num > 5:
        print(f"{num} è maggiore di 5")
    elif num == 5:
        print(f"{num} è uguale a 5")
    else:
        print(f"{num} è minore di 5")

if __name__ == "__main___":

    mynum = check_value(num = int(input("inserisci numero: ")))
