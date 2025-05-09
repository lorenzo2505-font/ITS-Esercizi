'''8-5. Città: scrivi una funzione chiamata describe_city() che accetti il ​​nome di una città e il suo paese.
 La funzione dovrebbe stampare una frase semplice, come Reykjavik è in Islanda. Assegna un valore predefinito al parametro per il paese. 
 Chiama la tua funzione per tre città diverse, almeno una delle quali non si trovi nel paese predefinito.'''

def describe_city (città: str, paese: str = "Italia"):
    print(f"{città} si trova in {paese}")

describe_city ("Roma")
describe_city ("Firenze")
describe_city ("Londra", "Inghilterra")
    