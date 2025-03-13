'''8-13. Profilo utente:
 crea un profilo di te stesso chiamando build_profile(), usando il tuo nome e cognome e altre tre coppie chiave-valore che ti descrivono. 
 Tutti i valori devono essere passati alla funzione come parametri. 
 La funzione deve quindi restituire una stringa come "Eric Crow, età 45, capelli castani, peso 67"'''

def build_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

build_profile (nome = "Lorenzo", cognome = "Acomanni")