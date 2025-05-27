'''Inizia definendo una classe base astratta chiamata Shape.
 Questa classe dovrebbe includere due metodi astratti: uno denominato area, che sarà responsabile del calcolo dell'area di una forma,
   e un altro denominato perimeter, che calcolerà il perimetro.
   Poiché Shape è astratta, non fornirà implementazioni specifiche per questi metodi. 
   Piuttosto, imposta un modello per tutte le forme che erediteranno da essa.

Quindi, crea due sottoclassi concrete, Circle e Rectangle, 
che estendono entrambe la classe Shape. 
Ognuna di queste sottoclassi deve fornire la propria implementazione dei metodi area e perimetro, 
basata sulle formule geometriche appropriate per le rispettive forme.

Infine, scrivi un semplice programma driver (codice di test) che crei istanze di Circle e Rectangle, 
richiami i loro metodi area e perimetro e ne stampi i risultati.
 Questo ti aiuterà a verificare che la gerarchia delle classi funzioni come previsto.'''



from abc import ABC, abstractmethod



class Shape(ABC):


    @abstractmethod

    def area(self):
        
        pass
    
    @abstractmethod

    def perimeter(self):
        
        pass




class Circle(Shape):
    
  def __init__(self, r: float):
    super().__init__()   

    self.set_r(r) 
      
  def set_r(self, r: float):
          
    if r < 0:
              
      raise ValueError ("il raggio non può essere negativo")
          
    else:
              
      self._r = r
  
  def get_r(self):
     
    return self._r
  
  def area(self):
     
    area: float = (self._r ** 2) * (3.14)

    return f"{area:.1f}"
  
  def perimeter(self):

    perimeter: float = 2 * self._r * 3.14

    return f"{perimeter:.1f}"



c: Circle = Circle(5.0)

print(c.area())

print(c.perimeter())



class Rectangle(Shape):
   
  def __init__(self, b: float, h: float):
    super().__init__()

    self.set_b(b)

    self.set_h(h)
    
  def set_b(self, b: float):

    if b < 0:

      raise ValueError("la base non può essere negativa")
    
    else:

      self._b = b
  
  def set_h(self, h: float):

    if h < 0:

      raise ValueError("l'altezza non può essere negativa")
    
    else:

      self._h = h
  
  def area(self):

    area: float = self._b * self._h

    return area

  def perimeter(self):

    perimeter: float = (self._b * 2) + (self._h * 2)

    return perimeter
  


r: Rectangle = Rectangle(5.0, 3.0)

print(r.area())

print(r.perimeter())
  


   

   

   

    
     
     

     
    

   

        




    


