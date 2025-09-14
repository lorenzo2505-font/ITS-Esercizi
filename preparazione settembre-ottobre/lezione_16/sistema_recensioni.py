class Media:

    def __init__(self, title: str):
        
        self.set_title(title)
        self.reviews: list[int] = []
    
    def set_title(self, title: str):

        if title:
            self.title = title
        
        else:

            raise ValueError("inserire un titolo valido")
    
    def get_title(self) -> str:

        return self.title
    
    def aggiungiValutazione(self, voto: int):

        if voto not in range(1, 5 + 1):

            raise ValueError("il voto deve avere un valore compreso tra 1 e 5")
        
        self.reviews.append(voto)
    
    def getMedia(self) -> int | float:

        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self, m: int | float) -> str:

        

        if 1 <= m < 2:

            return "Terribile"
        
        elif 2 <= m < 3:

            return "Brutto"
        
        elif 3 <= m < 4:

            return "Normale"
        
        elif 4 <= m < 5:

            return "Bello"
        
        elif m == 5:

            return "Grandioso"
    
    def getPercentage(self, voto: int):
        
        counter = 0

        for i in self.reviews:

            if i == voto:
                counter += 1
        
        return (counter * 100) / len(self.reviews)
    
    def recensione(self):

        print(f"Titolo del Film: {self.title}")
        print(f"Voto Medio: {self.getMedia()}")
        
        for i in range(1, 5 + 1):
            print(f"{self.getRate(i)}: {self.getPercentage(i)}")

class Film(Media):

    def __init__(self, title: str):
        super().__init__(title)



def main():

    il_popa_oscuro: Film = Film("il popa oscuro")
    
    for i in range(1, 10 + 1):

        if i > 5:
            i = i // 2

        il_popa_oscuro.aggiungiValutazione(i)
    
    il_popa_oscuro.recensione()

        

    


main()



        

    
