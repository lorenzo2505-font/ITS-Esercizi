'''9-3. Utenti:
 crea una classe chiamata User. Crea due attributi chiamati first_name e last_name,
   quindi crea altri attributi che sono solitamente memorizzati in un profilo utente.
     Crea un metodo chiamato describe_user() che stampa un riepilogo delle informazioni dell'utente. 
     Crea un altro metodo chiamato greet_user() che stampa un saluto personalizzato all'utente.
       Crea diverse istanze che rappresentano utenti diversi e chiama entrambi i metodi per ogni utente.'''

class Utente:
    def __init__ (self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
