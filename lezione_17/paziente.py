from persona import Persona 


class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, idCode: str):
        super().__init__(first_name, last_name)
        self.setIdCode(idCode)
    
    def setIdCode(self, idCode: str):
        
        if idCode:
            self.__idCode = idCode
        
        else:
            raise ValueError('inserire un codice valido')
    
    def getIdCode(self) -> str:
        return self.__idCode
    
    def patientInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.__idCode}")
    





if __name__ == '__main__':

    p: Paziente = Paziente('Chandler', 'Chad', 'maso')
    p.patientInfo()
