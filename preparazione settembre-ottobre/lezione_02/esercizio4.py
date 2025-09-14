'''scrivere una funzione che accetti una stringa e un carattere di ricerca e restituisca il numero di volte in cui carattere appare nella stringa

ad esempio str: ciao c: o -> 1'''


def myfun4(mystr: str, c: str) -> int:

    counter = 0

    if len(c) > 1 or (not(c)):
        
        raise ValueError("la stringa c deve contenere non più o meno di un carattere")
    
    for i in range(len(mystr)):

        if mystr[i] == c:

            counter += 1
    
    return counter


s: str = "ciao"

print(myfun4(s, "o"))


