'''Scrivi una funzione validate_password(password) che verifichi se una password soddisfa i seguenti criteri:
 lunghezza minima di 20 caratteri, almeno tre lettere maiuscole, almeno quattro caratteri speciali (non alfanumerici).
   Se la password è valida, la funzione deve restituire True. Se la password non è valida,
     la funzione deve generare un'eccezione predefinita (ad esempio, ValueError) 
con un messaggio che indica quali criteri non sono stati soddisfatti.'''

'''import re

def validate_password (password: str):

    if len(password) >= 20 and re.findall(r"[A-Z] {3,}", password) in password and re.findall(r"\W {4,}", password) in password:
        return True
    else:
        return ValueError

print(validate_password("ABC####aaaaaaaaaaaaa"))'''


import re

def validate_password (password: str):

    caratteri_speciali = "!£$%&^?*#"

    conta_speciali = 0

    conta_maiuscoli = 0

    for i in password:
        if i.upper() in password:
            conta_maiuscoli += 1
        if i in caratteri_speciali:
            conta_speciali += 1

    print(conta_maiuscoli)
    print(conta_speciali)

validate_password ("ag#gUUU")
    

