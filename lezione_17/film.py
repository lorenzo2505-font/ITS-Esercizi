from __future__ import annotations

class Film:
    def __init__(self, id: int, title: str):
        self.setID(id)
        self.setTitle(title)
    
    def setID(self, id: int):
        
        if id <= 0:
            raise ValueError('inserire un id che abbia valore maggiore di zero')
        
        self.__id = id
    
    def setTitle(self, title: str):

        if title:
            self.__title = title
        
        else:
            raise ValueError('inserire un titolo valido')
    
    def getID(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, otherFilm: Film):

        if self.getID() == otherFilm.getID():
            return True
        
        return False
    

if __name__ == '__main__':
    
    superman: Film = Film(1, 'superman')
    the_batman: Film = Film(1, 'the batman')
    the_suicide_squad: Film = Film(2, 'the suicide squad')

    print(superman.isEqual(the_batman))
    print(superman.isEqual(the_suicide_squad))

    
