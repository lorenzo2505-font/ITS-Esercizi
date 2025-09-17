from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)

        if type(specialization) != str:
            self.specialization = None

            raise ValueError('la specializzazione non è inserita come stringa')
        
        if type(parcel) != float:
            self.parcel = None

            raise ValueError('la parcella non è inserita come numero reale')
        
        self.specialization = specialization
        self.parcel = parcel
    
    def setSpecialization(self, specialization: str):
        
        if type(specialization) != str:
            raise ValueError('la specializzazione non è inserita come stringa')
        
        self.specialization = specialization
    
    def setParcel(self, parcel: float):

        if type(parcel) != float:
            raise ValueError('la specializzazione non è inserita come stringa')
        
        self.parcel = parcel
    
    def getSpecialization(self) -> str:
        return self.specialization
    
    def getParcel(self) -> float:
        return self.parcel
    
    def isAValidDoctor(self) -> bool:

        if self.age > 30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
            
            return True
        
        else:
            print(f"Doctor {self.first_name} e {self.last_name} is not valid!")

            return False
    
    def doctorGreet(self):
        self.greet()
        print(f"sono un medico {self.specialization}")


if __name__ == '__main__':

    jd: Dottore = Dottore('John', 'Dorian', 'Di Base', 4000.0)
    jd.setAge(31)
    jd.isAValidDoctor()
    jd.doctorGreet()
        


    
    