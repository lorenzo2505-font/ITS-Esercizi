'''9-2. Tre ristoranti: 
inizia con la classe dell'esercizio 9-1.
 Crea tre istanze diverse dalla classe e chiama describe_restaurant() per ogni istanza.'''

class Ristorante:
    def __init__ (self, nome_ristorante, tipo_cucina):
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina

    def describe_resturant (self):
        print(f"{self.nome_ristorante}, {self.tipo_cucina}")

    def open_resturant (self):
        print("il ristorante è aperto")

siciliano = Ristorante ("A Lume Di Sicilia", "Cucina siciliana")
bottarolo = Ristorante ("Dar Bottarolo", "Cucina romana")
neko = Ristorante ("Neko", "Cucina orientale")

siciliano.describe_resturant ()
bottarolo.describe_resturant ()
neko.describe_resturant ()
