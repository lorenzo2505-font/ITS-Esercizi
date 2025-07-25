'''Validazione di un Indirizzo IPv4

Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.).

 Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.

Requisiti:
● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.

● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].
Esempi:

is_valid_ipv4("192.168.0.1") # True

is_valid_ipv4("255.255.255.255") # True

is_valid_ipv4("256.100.10.1") # False (256 è fuori range)

is_valid_ipv4("192.168.1") # False (solo 3 parti)

is_valid_ipv4("192.168.1.a") # False (parte non numerica)'''


import re


def is_valid_ipv4(adress: str ) -> bool:


    intervalliGiusti = 0


    if re.fullmatch(r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$", adress):

        for i in adress.split("."):

            if (i.isdigit()) and (0 <= int(i) <= 255) :

                intervalliGiusti += 1
    

        print(intervalliGiusti)

        if intervalliGiusti == 4:

            return True
        
        else:

            return False
    
    else:

        return False


test = is_valid_ipv4("192.168.0.1")

print(test)








# versione prof


def chekIP(ip: str) -> bool:

    ip = ip.split(".")

    if len(ip) != 4:

        #raise Exception("indirizzo mal formato")

        return False
    
    for blocco in ip:

        if not blocco.isdigit():

            #raise Exception("errore, l'indirizzo contiene un carattere alfabetico")

            return False
        
        if not (0 <= int(blocco) <= 255):

            return False
    
    return True


    