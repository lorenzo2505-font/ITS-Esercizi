from forma import Forma

class Triangolo(Forma):
    def __init__(self, lato: int):
        super().__init__('Triangolo')
        
        if lato == 0:
            raise ValueError('il lato non può avere valore 0')
        
        self.lato = lato
    
    def getArea(self) -> int:
        return self.lato * self.lato / 2
    
    def render(self):
        l = abs(self.lato)
        a = 1
        y = 0

        for x in range(l):
            print("")
            y += a
            for i in range(y):
                print("*", end="")


if __name__ == '__main__':

    t: Triangolo = Triangolo(4)
    print(t.getArea())
    t.render()