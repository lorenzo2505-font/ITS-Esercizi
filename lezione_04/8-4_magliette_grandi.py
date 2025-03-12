'''8-4. Magliette grandi: modifica la funzione make_shirt() in modo che le magliette siano grandi di default con un messaggio che recita I love Python.
 Crea una maglietta grande e una maglietta media con il messaggio di default e una maglietta di qualsiasi taglia con un messaggio diverso.'''

def make_shirt (taglia: str = "l", frase: str = "i love python" ):
    match taglia:
        case "xs"|"s"|"m"|"l"|"xl"|"xxl":
            print(taglia.upper())
            print(frase.title())
        case _ :
            print("errore: questa taglia non esiste")

make_shirt ()

make_shirt ("m")

make_shirt ("s", "i hate python")


