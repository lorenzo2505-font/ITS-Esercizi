class Alieno:
    '''
    sapere la gallassia di provenienza
    '''
    #inizializzare un concetto della classe alieno 
    def __init__(self, galaxy: str) -> None:
        self.setGalaxy(galaxy)

    #definire un metodo per impostare setGalaxy

    def setGalaxy(self, galaxy: str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("errore")

    #definire un metodo per restituire self.galaxy

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("io sono groot")
    
    def __str__(self):
        return f"alieno proveniente della galassia {self.getGalaxy()}"







        
    


    
    