'''PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo).
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, 
il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare.
Questa funzione dovrebbe aggiornare il dizionario del contatto.'''

def create_contact(nome: str,  email: str = None, telefono: int = None) -> dict:

    return {"nome": nome,  "email": email, "telefono": telefono}

def update_contact(mydict: dict, nome: str, email: str = None, telefono: int = None) -> dict:

    if telefono is not None:
        mydict["telefono"] = telefono
    
    if email is not None:
        mydict["email"] = email
    
    return mydict



contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))


