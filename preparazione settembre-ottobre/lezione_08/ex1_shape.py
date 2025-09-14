from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    
    def area():
        pass

    @abstractmethod

    def perimetro():
        pass

class Circle(Shape):
    
    def area(self, raggio: float):
        
        return round(raggio ** 2 * 3.14, 1)
    
    def perimetro(self, raggio: float):

        return round(2 * 3.14 * raggio, 1)


class Rectangle(Shape):

    def area(self, base: float, altezza: float):
        
        return round (base * altezza, 1)
    
    def perimetro(self, base: float, altezza: float):

        return round((base * 2) + (altezza * 2), 1)




def main():
    
    c: Circle = Circle()
    print(c.area(5.0))
    print(c.perimetro(5.0))

    r: Rectangle = Rectangle()
    print(r.area(4, 3))
    print(r.perimetro(4, 3))

main()
    


    