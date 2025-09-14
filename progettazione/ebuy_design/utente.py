from __future__ import annotations

from custom_types import *

from abc import *

from datetime import *


class Utente(ABC):

    _username: str # noto alla nascita
    
    _registrazione: datetime # <<immutable>> noto alla nascita
    
    @abstractmethod

    def __init__(self, username: str, registrazione: datetime):
        super().__init__()

        self.setUsername(username)
        
        self._registrazione = registrazione


    
    def username(self) -> str:

        return self._username
    
    def registrazione(self) -> datetime:

        return self._registrazione
    
    def setUsername(self, username: str):
        
        if username:

            self._username = username
        
        else:

            raise ValueError("inserire uno username valido")
    
    def __str__(self):
        return super().__str__() + f"username: {self._username}\nregistrazione: {self._registrazione}"
    
    def popolarità(i: datetime):
        pass
    
    def affidabilità(i: datetime) -> RealZO:
        pass

    
    
    




        


    
    
        

    






    
