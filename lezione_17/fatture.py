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
        return len(self.pazienti)
    
    def addPatient(self, newPatient: Paziente):

        if newPatient in self.pazienti:
            raise ValueError("il paziente è gia presente nell'elenco")
        
        self.pazienti.append(newPatient)
        f = self.getFatture()
        s = self.getSalary()
        print(f"fattura: {f}, salario: {s}")
        print(f"Alla lista del Dottor {self.dottore.last_name} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode: str):
        counter = 0
        
        for i in self.pazienti:
            
            if i.getIdCode() == idCode:
                self.pazienti.remove(i)
                f = self.getFatture()
                s = self.getSalary()
                print(f'fattura: {f}, salario: {s}')
                print(f"Alla lista del Dottor {self.dottore.last_name} è stato rimosso il paziente {idCode}")
                break

            else:
                counter += 1
        
        if counter == len(self.pazienti):
            raise ValueError("il paziente non è presente nell'elenco")



if __name__ == '__main__':
    
    jd: Dottore = Dottore('john', 'dorian', 'di base', 5000.0)
    jd.setAge(31)

    turk: Dottore = Dottore('christopher', 'turk', 'chirurgo', 5000.0)
    turk.setAge(31)

    p1: Paziente = Paziente('marco', 'pierleoni', 'pierlions')
    p1.setAge(27)

    p2: Paziente = Paziente('lorenzo', 'rossi', 'crazy')
    p2.setAge(20)

    p3: Paziente = Paziente('alessandro', 'popa', 'dacho_noj')
    p3.setAge(21)

    p4: Paziente = Paziente('erald', 'cancka', 'zio')
    p4.setAge(37)

    jd_list: list[Paziente] = [p1, p2, p3]
    turk_list: list[Paziente] = [p4]

    jd.doctorGreet()
    turk.doctorGreet()

    jd_fattura: Fattura = Fattura(jd_list, jd)
    turk_fattura: Fattura = Fattura(turk_list, turk)

    print(f'salario del dottor {jd.last_name}: {jd_fattura.getSalary()} euro')
    print(f'salario del dottor {turk.last_name}: {turk_fattura.getSalary()} euro')

    jd_fattura.removePatient('pierlions')
    turk_fattura.addPatient(p1)

    print(f"In totale, l'ospedale ha incassato: {jd_fattura.getSalary() + turk_fattura.getSalary()} euro!")

    



    



        
        
        
