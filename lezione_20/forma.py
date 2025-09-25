from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome: str):
        super().__init__()
        self.nome = nome
    
    @abstractmethod
    def getArea():
        pass

    @abstractmethod
    def render():
        pass

