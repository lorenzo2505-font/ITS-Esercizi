'''Scrivi una funzione check_length(), che accetta una stringa come argomento.
Usando if / else, controlla se la lunghezza della stringa è maggiore, minore o uguale a 10 caratteri'''

def check_lenght(parola: str):
    if len(parola) > 10:
        print("la parola ha più di 10 caratteri")
    elif len(parola) < 10:
        print("la parola ha meno di 10 caratteri")
    else:
        print("la parola ha 10 caratteri")
myword = check_lenght(parola = str(input("inserisci parola: ")))

    
