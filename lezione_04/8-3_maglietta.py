'''8-3. Maglietta: scrivi una funzione chiamata make_shirt() che accetti una taglia e il testo di un messaggio che 
dovrebbe essere stampato sulla maglietta. 
La funzione dovrebbe stampare una frase che riassuma la taglia della maglietta e il messaggio stampato su di essa. 
Chiama la funzione una volta usando argomenti posizionali per creare una maglietta. Chiama la funzione una seconda volta usando
 argomenti per parole chiave.'''

def make_shirt (taglia: str, frase: str ):
    match taglia:
        case "xs"|"s"|"m"|"l"|"xl"|"xxl":
            print(taglia.upper())
            print(frase.title())
        case _ :
            print("errore: questa taglia non esiste")
make_shirt("xs", "adidas")

make_shirt (frase = "nike", taglia = "s")
    