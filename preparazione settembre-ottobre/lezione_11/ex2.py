class Prodotto:

    def __init__(self, nome: str, quantità: int):
        
        self.nome = nome
        self.quantità = quantità



class Magazzino:

    def __init__(self):
        
        self.prodotti: list[Prodotto] = []
    
    def aggiungi_prodotto(self, prodotto: Prodotto):

        if prodotto in self.prodotti:

            raise ValueError("il prodotto è presente nell'elenco")
        
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome: str) -> Prodotto|None:

        for i in self.prodotti:

            if i.nome == nome:
                
                return i
        
        return None
    
    def verifica_disponibilità(self, nome: str) -> str:

        v = self.cerca_prodotto(nome)

        if v == None:
            return "Prodotto non disponibile"
        
        return "prodotto disponibile"

        
    

def main():

    c_popa: Prodotto = Prodotto("canna del popa", 2)

    cappello_pierlions: Prodotto = Prodotto("cappello di pierlions", 1)

    pc_cutolo: Prodotto = Prodotto("pc di cutolo", 1)

    magazzino_its: Magazzino = Magazzino()

    magazzino_its.aggiungi_prodotto(c_popa)
    magazzino_its.aggiungi_prodotto(cappello_pierlions)
    magazzino_its.aggiungi_prodotto(pc_cutolo)

    print(magazzino_its.cerca_prodotto("canna del popa"))
    print(magazzino_its.verifica_disponibilità("pc di cutolo"))

main()

                
        
    

