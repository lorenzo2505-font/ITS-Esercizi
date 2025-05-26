'''Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:
Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
Il sistema cerca un prodotto per verificare se esiste nell'inventario.
Il sistema verifica la disponibilità dei prodotti in inventario.'''



class Prodotto:

    def __init__(self, nome: str, quantità: int):
        
        self.set_nome(nome)

        self.set_quantità(quantità)

    
    def set_nome(self, nome: str):

        if nome:

            self.nome = nome
        
        else:

            raise Exception("inserire un nome valido")
    
    def set_quantità(self, quantità: int):


        if quantità < 0:

            raise Exception("la quantità non può essere negativa")
        
        else:

            self.quantità = quantità
    
    def get_nome(self):

        return self.nome
    
    def get_quantità(self):

        return self.quantità
    
    def __str__(self):

        return f"nome prodotto: {self.nome}, quantità: {self.quantità}"
    

p: Prodotto = Prodotto("penna", 2)

#print(p)
        

class Magazzino:

    def __init__(self):
        
        self.prodotti: list [Prodotto] = []

    
    def aggiungi_prodotto(self, prodotto: Prodotto):

        if self.prodotti == []:

            self.prodotti.append(prodotto)

            print("aggiunta eseguita con successo")
        
        else:

            for i in self.prodotti:

                if i.get_nome() == prodotto.get_nome():

                    raise Exception("questo prodotto è già presente")
                
                else:

                    self.prodotti.append(prodotto)

                    print("aggiunta eseguita con successo")


    def cerca_prodotto(self, nome: str) -> Prodotto:

        for i in self.prodotti:

            if i.get_nome() == nome:

                return i
    
    def verifica_disponibilità(self, nome: str) -> str:

        for i in self.prodotti:

            if (i.get_nome() == nome) and (i.get_quantità() > 0):

                return "prodotto disponibile"


m: Magazzino = Magazzino()

m.aggiungi_prodotto(p)


print(m.cerca_prodotto("penna"))

print(m.verifica_disponibilità("penna"))




            


    

        
        
