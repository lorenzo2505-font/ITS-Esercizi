from custom_types import *
from datetime import date

class Partita:
    _data: date # noto alla nascita
    _indirizzo: Indirizzo # noto alla nascita
    _komi: Komi # <<immutable>> noto alla nascita
    
    def __init__(self, data: date, indirizzo: Indirizzo, komi: Komi):
        self.setData(data)
        self.setIndirizzo(indirizzo)
        self._komi = komi
    
    def setData(self, data: date):
        self._data = data
    
    def setIndirizzo(self, indirizzo: Indirizzo):
        self._indirizzo = indirizzo
    
    def getData(self):
        return self._data
    
    def getIndirizzo(self):
        return self._indirizzo
    
    def getKomi(self):
        return self._komi
    
    def __str__(self):
        return f'data della partita: {self._data}, indirizzo: {self._indirizzo}, komi: {self._komi}'


if __name__ == '__main__':

    partitone: Partita = Partita(date(2026, 7, 9), Indirizzo('viale cesare pavese', 305), 5.5)
    print(partitone)

