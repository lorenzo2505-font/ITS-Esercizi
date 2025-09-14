import random

class Creatura:

    def __init__(self, nome: str):
        
        self.setNome(nome)
    
    def setNome(self, nome: str):

        if nome:
            self.__nome = nome
        
        else:
            self.__nome = "Creatura Generica"
    
    def getNome(self) -> str:

        return self.__nome
    
    def __str__(self) -> str:

        return f"Creatura: {self.__nome}"

class Alieno(Creatura):

    def __init__(self, nome: str):
        super().__init__(nome)

        self.__setMatricola()
        self.__setMunizioni()

        if self.getNome() != f"Robot-{self.__matricola}":
            print("Attenzione! Tutti gli Alieni devono avere il nome Robot seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            
            self.setNome(f"Robot-{self.__matricola}")
    
    def __setMatricola(self):

        self.__matricola = random.randint(10000, 90000)
    
    def __setMunizioni(self):

        self.__munizioni: list[int] = [x**2 for x in range(15)]
    
    def getMatricola(self) -> int:

        return self.__matricola
    
    def getMunizioni(self):

        return self.__munizioni
    
    def __str__(self):
        return f"Alieno: {self.getNome()}"

class Mostro(Creatura):

    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str):
        super().__init__(nome)

        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self.__setAssalto()
    
    def __setVittoria(self, urlo_vittoria: str):

        if urlo_vittoria != "GRAAAHHH":
            self.__vittoria = "GRAAAHHH"
        
        else:
            self.__vittoria = urlo_vittoria
    
    def __setSconfitta(self, gemito_sconfitta: str):

        if gemito_sconfitta != "Uuurghhh":
            self.__sconfitta = "Uuurghhh"
        
        else:
            self.__sconfitta = gemito_sconfitta
    
    def __setAssalto(self):

        self.__assalto: list[int] = [] 

        while True:
            n = random.randint(1, 100)

            if n not in self.__assalto:
                self.__assalto.append(n)
            
            if len(self.__assalto) == 15:
                break
    
    def getVittoria(self):

        return self.__vittoria
    
    def getSconfitta(self):

        return self.__sconfitta
    
    def getAssalto(self):

        return self.__assalto
    
    def __str__(self):
        
        new_name: str = ""
        original_name = self.getNome().lower()

        for i in range(len(original_name)):

            if i % 2 != 0:
                new_name += original_name[i].upper()
            
            else:
                new_name += original_name[i]
        
        return f"Mostro: {new_name}"

def pariUguali(a: list[int], b: list[int]) -> list[int]:

    c: list[int] = []
    
    if len(a) != len(b):

        raise ValueError("le liste devono avere la stessa lunghezza")
    
    for i in range(len(a)):

        if a[i] < 0 or b[i] < 0:
            
            raise ValueError("le liste devono contenere interi positivi")
        
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        
        else:
            c.append(0)
    
    return c

def combattimento(a: Alieno, m: Mostro):

    counter = 0
    
    if type(a) != Alieno or type(m) != Mostro:

        raise TypeError("a o m non sono stati istanziati correttamente\na deve essere un oggetto della classe Alieno\nm deve essere un oggetto della classe Mostro")
    
    p = pariUguali(a.getMunizioni(), m.getAssalto())

    for i in p:

        if i == 1:
            counter += 1
    
    if counter > 4:
        print(m.getVittoria())
        print(m.getVittoria())
        print(m.getVittoria())

        return m
    
    else:
        print(m.getSconfitta())

        return a


def proclamaVincitore(c: Creatura):

    w: int = len(c.__str__()) + 10
    h: int = 5
    testo = str(c)

    for i in range(w):
        print("*", end="")
    
    print()

    for j in range(h - 2):

        if j == (h - 2) // 2:   
            spazi = (w - 2 - len(testo)) // 2
            print("*" + " " * spazi + testo + " " * (w - 2 - len(testo) - spazi) + "*")

        else:
            print("*", end="")

            for i in range(w - 2):
                print(" ", end="")

            print("*")

    
    for i in range(w):
        print("*", end="")

    print()








        
    

        
        

    


            
    
    



    
    
    

    
    

    

        

def main():
    
    creatura: Creatura = ("")
    print(creatura)

    alieno: Alieno = Alieno("Robot-popa")
    print(alieno)

    mostro: Mostro = Mostro("black pierre", "", "")
    print(mostro)

    c = combattimento(alieno, mostro)

    proclamaVincitore(c)

    

    

main()
    

    

    

    
