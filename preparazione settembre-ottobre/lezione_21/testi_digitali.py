import re

class Documento:

    def __init__(self, testo: str):
        
        self.setText(testo)
    
    def setText(self, testo: str):

        if testo:
            self.testo = testo
        
        else:

            raise ValueError("inserire un testo valido")
    
    def getText(self) -> str:

        return self.testo
    
    def isInText(self, parola: str) -> bool:

        if parola in self.testo.split(" "):

            return True
        
        return False
    
class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str):
        super().__init__(testo)

        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo)
    
    def setMittente(self, mittente: str):

        if re.fullmatch(r"^\S+@\S+\.\S+$", mittente):
            self.mittente = mittente
        
        else:
            
            raise ValueError("inserire una email valida per il mittente")
    
    def setDestinatario(self, destinatario: str):

        if re.fullmatch(r"^\S+@\S+\.\S+$", destinatario):
            self.destinatario = destinatario
        
        else:

            raise ValueError("inserire una email valida per il destinatario")
    
    def setTitolo(self, titolo: str):

        if titolo:
            self.titolo = titolo
        
        else:

            raise ValueError("inserire un titolo per l'email valido")
    
    def getText(self) -> str:
        
        return f"Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}"
    
    def getMittente(self) -> str:

        return self.mittente
    
    def getDestinatario(self) -> str:

        return self.destinatario
    
    def getTitolo(self) -> str:

        return self.titolo
    
    def writeToFile(self) -> str:

        text = self.getText()
        
        with open("lezione_21/email1.txt", "w") as f:
            f.write(text)
    


class File(Documento):

    def __init__(self, nomePercorso: str):
        
        self.nomePercorso = nomePercorso

        super().__init__(self.leggiTestoDaFile())
    
    def leggiTestoDaFile(self):
        
        with open(f"{self.nomePercorso}/document.txt", "r") as f:
            t = f.read()
        
        return t
    
    def getText(self):

        return f"Percorso: {self.nomePercorso}/document.txt\n Contenuto: {super().getText()}"







def main():

    email: Email = Email("bosco merda", "popa.torvaianica@gmail.canna", "marco.pierlions@metal.com", "Bosco M")
    file: File = File("lezione_21")

    print(email.getText())
    print(file.getText())

    email.writeToFile()

    print(email.isInText("incontrarci"))
    print(file.isInText("percorso"))

main()
    

    

        
    
    