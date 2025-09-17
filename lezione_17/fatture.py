from paziente import Paziente
from dottore import Dottore

class Fattura:

    def __init__(self, pazienti: list[Paziente], dottore: Dottore):

        if dottore.isAValidDoctor():
            self.fatture: int = len(pazienti)
            self.salary: int = 0
            self.pazienti = pazienti
            self.dottore = dottore
        
        else:
            self.pazienti = None
            self.dottore = None
            self.fatture = None
            self.fatture = None

            raise Exception('Non è possibile creare la classe fattura poichè il dottore non è valido!')
    
    def getSalary(self) -> float:
        self.salary = self.dottore.getParcel() * len(self.pazienti)

        return self.salary
    
    def getFatture(self) -> int:
        return self.fatture
    
    def addPatient(self, newPatient: Paziente):

        if newPatient in self.pazienti:
            raise ValueError("il paziente è gia presente nell'elenco")
        
        self.pazienti.append(newPatient)
        
        
