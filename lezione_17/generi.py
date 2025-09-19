from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = 'Azione'
        self.__penale: str = 3.0
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni: int):

        if giorni < 0:
            raise ValueError('inserire un numero di giorni maggiore o uguale a zero')
        
        res = self.__penale * giorni 
        
        return res


class Commedia(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = 'Commedia'
        self.__penale: str = 2.5
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni: int):

        if giorni < 0:
            raise ValueError('inserire un numero di giorni maggiore o uguale a zero')
        
        res = self.__penale * giorni 
        
        return res


class Drama(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = 'Drama'
        self.__penale: str = 2.0
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni: int):

        if giorni < 0:
            raise ValueError('inserire un numero di giorni maggiore o uguale a zero')
        
        res = self.__penale * giorni 
        
        return res

