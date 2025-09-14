class Persona:

    persone = []

    def __init__(self, nome, età):
        
        self.nome = nome
        self.età = età
        self.persone.append(self)
    
    @classmethod # metodo che coinvolgono la classe

    def quante_persone(cls):
        
        return len(cls.persone)
    
    @staticmethod # metodo che non coinvolge gli attributi di una classe

    def parla(x):
        for i in range(x):
            print("ciao")


mauro = Persona("mauro", 20)
pippo = Persona("pippo", 45)

print(Persona.quante_persone()) # si può anche fare con un'istanza di classe