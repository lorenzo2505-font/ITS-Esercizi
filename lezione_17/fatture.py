from paziente import Paziente
from dottore import Dottore

class Fattura:

    def __init__(self, pazienti: list[Paziente], dottore: Dottore):

        if dottore.isAValidDoctor():
            self.fatture: int = len(pazienti)
        
