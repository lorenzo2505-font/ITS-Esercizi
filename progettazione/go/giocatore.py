from custom_types import *

class Giocatore:
    _nickname: str # noto alla nascita
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita 
    _indirizzo: Indirizzo # noto alla nascita
    _rank: IntGZ # noto alla nascita

    def __init__(self, nickname: str, nome: str, cognome: str, indirizzo: Indirizzo, rank: IntGZ):
        self.setNickname(nickname)
        self.setNome(nome)
        self.setCognome(cognome)
        self.setIndirizzo(indirizzo)
        self.setRank(rank)
    
    def setNickname(self, nickname: str):
        
        if nickname:
            self._nickanme = nickname
        
        else:
            raise ValueError('inserire un nickname valido')
    
    def setNome(self, nome: str):

        if nome:
            self._nome = nome
        
        else:
            raise ValueError('inserire un nome valido')
    
    def setCognome(self, cognome: str):

        if cognome:
            self._cognome = cognome
        
        else:
            raise ValueError('inserire un cognome valido')
    
    def setIndirizzo(self, indirizzo: Indirizzo):
        self._indirizzo = indirizzo
    
    def setRank(self, rank: IntGZ):
        self._rank = rank
    
    def getNickname(self) -> str:
        return self._nickanme
    
    def getNome(self) -> str:
        return self._nome
    
    def getCognome(self) -> str:
        return self._cognome
    
    def getIndirizzo(self):
        return self._indirizzo
    
    def getRank(self):
        return self._rank
    
    def __str__(self):
        return f"nickname giocatore: {self._nickanme},\nnome: {self._nome},\ncognome: {self._cognome},\nindirizzo; {self._indirizzo},\nrank: {self._rank}"


if __name__ == '__main__':

    giuliano: Giocatore = Giocatore('pisellone95', 'Giuliano', 'Liscaio', Indirizzo('via fonteiana', 111), 1)
    print(giuliano)
    

