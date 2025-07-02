import random

class Media:

    def __init__(self, title: str):
        
        self.set_title(title)

        self.reviews: list[int] = []

    def set_title(self, title: str) -> None:

        if title:

            self.title = title
        
        else:

            raise ValueError("inserire un titolo valido")
    
    def get_title(self) -> str:

        return self.title
    
    def aggiungiValutazione(self, voto: int) -> None:

        if 1 <= voto <= 5:

            self.reviews.append(voto)
        
        else:

            raise ValueError("il voto deve essere tra 1 e 5 compresi")
    
    def getMedia(self) -> float:

        voto_medio = sum(self.reviews) / len(self.reviews)

        return voto_medio
    
    def getRate(self, v: int|float) -> str:

        if 1 <= v < 2:

            return "terribile"
        
        elif 2 <= v < 3:

            return "brutto"
        
        elif 3 <= v < 4:

            return "normale"
        
        elif 4 <= v < 5:

            return "bello"
        
        else:

            return "grandioso"
    
    def ratePercentage(self, voto: int) -> str:

        if voto not in self.reviews:

            raise ValueError("il voto non è presente nell'elenco")
        
        else:

            percentuale = voto * 100 / 5

            return f"{percentuale}%"
        
        
    
    def recensione(self) -> None:

        print(f"titolo: {self.title}")

        print(f"voto medio: {self.getMedia()}")

        print(f"giudizio: {self.getRate(self.getMedia())}")

        for i in self.reviews:

            print(f"{self.getRate(i)}: {self.ratePercentage(i)}")





class Film(Media):

    def __init__(self, title: str):
        super().__init__(title)








f1: Film = Film ("il cavaliere oscuro")



for i in range(1, 10 + 1):

    n: int = random.randint(1, 5)

    f1.aggiungiValutazione(n)


f1.recensione()



f2: Film = Film("cast away")


for i in range(1, 10 + 1):

    n: int = random.randint(1, 5)

    f2.aggiungiValutazione(n)



f2.recensione()





            
        



    
        


    
