from forma import Forma

class Quadrato(Forma):
    def __init__(self, lato: int):
        super().__init__('Quadrato')
        
        if lato == 0:
            raise ValueError('il lato non può avere valore 0')
        
        self.lato = lato
    
    def getArea(self) -> int:
        return self.lato**2
    
    def render(self):
        l = abs(self.lato)

        for col in range(l):
            print("*", end="")
        print()

        for raw in range(l - 2):
            print("*", end="")
            for col in range(l - 2):
                print(" ", end="")
            print("*")
        
        for col in range(l):
            print("*", end="")
        print()


if __name__ == '__main__':

    q: Quadrato = Quadrato(4)
    print(q.getArea())
    q.render()
    
