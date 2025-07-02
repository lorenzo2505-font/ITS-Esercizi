import re


class Documento:

    def __init__(self, testo: str):
        
        self.setTesto(testo)

    
    def setTesto(self, testo: str):

        self.testo = testo
    
    
    def getTesto(self):

        return self.testo
    
    def isInText(self, parola: str) -> bool:

        if parola in self.testo.split(" "):

            return True
        
        else:

            return False







class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo_messaggio: str):
        super().__init__(testo)

        self.setMittente(mittente)

        self.setDestinatario(destinatario)

        self.setTitoloMessaggio(titolo_messaggio)

    
    def setMittente(self, mittente: str):

        if re.fullmatch(r"^\S+@\S+\.\S+$", mittente):

            self.mittente = mittente
        
        else:

            raise ValueError("inserie un mittete valido")
    
    def setDestinatario(self, destinatario: str):

        if re.fullmatch(r"^\S+@\S+\.\S+$", destinatario):

            self.destinatario = destinatario 
        
        else:

            raise ValueError("inserire un destinatario valido")
    
    def setTitoloMessaggio(self, titolo_messaggio: str):

        if titolo_messaggio:

            self.titolo_messaggio = titolo_messaggio
        
        else:

            raise ValueError("inserire un titolo valido")
    
    def getMittente(self):

        return self.mittente
    
    def getDestinatario(self):

        return self.destinatario
    
    def getTitoloMessaggio(self):

        return self.titolo_messaggio
    
    def getTesto(self):
        return f"da:{self.mittente} a: {self.destinatario}\ntitolo: {self.titolo_messaggio}\nmessaggio: {super().getTesto()}"
    
    def writeToFile(self):

        with open("lezione_21/email.txt", "w") as file:

            file.write(self.getTesto())









class File (Documento):

    def __init__(self, nomePercorso: str):

        self.nomePercorso = nomePercorso

        super().__init__(self.leggiTestoDaFile())

        

    
    def leggiTestoDaFile(self):

        with open(f"{self.nomePercorso}/document.txt", "r") as file:

            testo = file.read()
        
        return testo
        
        
    

    def getTesto(self):
        return f"percorso: {self.nomePercorso}/document.tx\ncontenuto: {super().getTesto()}"




email: Email = Email("m / s", "acomanni.lorenzo@iiscaffe.it", "alessandro.maiorana@iiscaffe.it", "unità di misura della velocità")

file: File = File ("lezione_21")

print(email.getTesto())

print(file.getTesto())

email.writeToFile()

print(email.isInText("incontrarci"))

print(file.isInText("percorso"))






    






    
    
        





