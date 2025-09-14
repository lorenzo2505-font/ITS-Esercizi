'''Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.

Requisiti:
● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.
● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].


'''


def is_valid_ipv4(address: str) -> bool:

    punti = 0
    correct_numbers = 0

    for i in address:

        if i == ".":
            punti += 1
    
    if punti != 3:
        
        return False
    
    for i in address.split("."):

        if (i.isdigit()) and (0 <= int(i) <= 255):
            correct_numbers += 1
    
    if correct_numbers != 4:

        return False
    
    return True

ip: str = "255.255.255.255"
print(is_valid_ipv4(ip))

             

