class Media:

    def __init__(self, title: str):
        
        self.set_title(title)

        self.reviews: list[int] = []

    def set_title(self, title: str):

        if title:

            self.title = title
        
        else:

            raise ValueError("inserire un titolo valido")
    
    def get_title(self):

        return self.title
    
    def aggiungiValutazione(self, voto: int):

        if 1 <= voto <= 5:

            self.reviews.append(voto)
        
        else:

            raise ValueError("il voto deve essere compreso tra 1 e 5 compresi")
    
    def getMedia(self):

        voto_medio = sum(self.reviews) / len(self.reviews)

        return voto_medio
    
    def getRate(self):

        if 1 <= self.getMedia() < 2:

            return "terribile"
        
        elif 2 <= self.getMedia() < 3:

            return "brutto"
        
        elif 3 <= self.getMedia() < 4:

            return "normale"
        
        elif 4 <= self.getMedia() < 5:

            return "bello"
        
        else:

            return "grandioso"
    
    def ratePercentage(self, voto):

        if voto in self.reviews:

            percentuale = voto * 100 / 5

            return f"{percentuale}%"
        
        else:

            raise ValueError("il voto non è nell'elenco")
    
    def recensione(self):
        pass


    
        


    
