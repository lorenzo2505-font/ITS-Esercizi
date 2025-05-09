'''9-1. Ristorante: 
crea una classe chiamata Ristorante.
 Il metodo __init__() per Ristorante dovrebbe memorizzare due attributi: un restaurant_name e un cuisine_type.
   Crea un metodo chiamato describe_restaurant() che stampi queste due informazioni 
   e un metodo chiamato open_restaurant()
     che stampi un messaggio che indica che il ristorante è aperto.
 Crea un'istanza chiamata ristorante dalla tua classe. Stampa i due attributi singolarmente e poi chiama entrambi i metodi.'''

class Ristorante:
    def __init__ (self, nome_ristorante, tipo_cucina):
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina

    def describe_resturant (self):
        print(f"{self.nome_ristorante}, {self.tipo_cucina}")

    def open_resturant (self):
        print("il ristorante è aperto")

siciliano = Ristorante ("A Lume Di Sicilia", "Cucina siciliana")

print(siciliano.nome_ristorante)
print(siciliano.tipo_cucina)

siciliano.describe_resturant ()
siciliano.open_resturant ()


    
