from forma import Forma

class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__('Rettangolo')

        if base == 0 or altezza == 0:
            raise ValueError(f'base e altezza non possono avere valore 0, attuale valore base: {base}, attuale valore altezza: {altezza}')
        
        self.base = base
        self.altezza = altezza
    
    def getArea(self) -> int:
        return self.base * self.altezza
    
    def render(self):
        b = abs(self.base)
        h = abs(self.altezza)

        for col in range(b):
            print("*", end="")
        print()

        for row in range(h - 2):
            print("*", end="")
            for col in range(b - 2):
                print(" ", end="")
            print("*")
        
        for col in range(b):
            print("*", end="")
        print()


if __name__ == '__main__':

    r: Rettangolo = Rettangolo(8, 4)
    print(r.getArea())
    r.render()
