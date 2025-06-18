


import random


class Creatura:

    def __init__(self, nome: str):

        self.setNome(nome)
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            self._nome = "Creatura Generica"
    
    def getNome(self):

        return self._nome
    
    def __str__(self):
        
        return f"nome creatura: {self._nome}"



class Alieno(Creatura):


    def __init__(self, nome: str):

        super().__init__(nome)

        self._setMatricola()

        
        self._setMunizioni()

        if nome != f"Robot-{self._matricola}":

            print("Attenzione! Tutti gli Alieni devono avere il nome Robot seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

            self._nome = f"Robot-{self._matricola}"
        
        else:

            self._nome = nome







        
    

    def _setMatricola(self):


        n: int = random.randint(10000, 90000)

        self._matricola = n
    
    def _setMunizioni(self):

        munizioni: list[int] = [i ** 2 for i in range(0, 15)]

        self._munizioni = munizioni
    
    
    

    def getMatricola(self):

        return self._matricola
    
    def getMunizioni(self):

        return self._munizioni
    
    
    
    def __str__(self):
        return f"Alieno: {self._nome}"
    


class Mostro(Creatura):

    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str):
        super().__init__(nome)

        self._setVittoria(urlo_vittoria)

        self._setSconfitta(gemito_sconfitta)

        self._setAssalto()
    
    def _setVittoria(self, urlo_vittoria: str):

        if urlo_vittoria != "GRAAAHHH":

            self._vittoria = "GRAAAHHH"
        
        else:

            self._vittoria = urlo_vittoria
    
    def _setSconfitta(self, gemito_sconfitta: str):

        if gemito_sconfitta != "Uuurghhh":

            self._sconfitta = "Uuurghhh"
        
        else:

            self._sconfitta = gemito_sconfitta
    
    def _setAssalto(self):

        assalto: list[int] = []

        while len(assalto) != 15:

            i = random.randint(1, 100)

            if i not in assalto:

                assalto.append(i)

        
        self._assalto = assalto

    def getVittoria(self):

        return self._vittoria
    
    def getSconfitta(self):

        return self._sconfitta
    
    def getAssalto(self):

        return self._assalto
    
    def __str__(self):


        new_name = ""

        for i in range(len(self._nome)):

            if i % 2 != 0:

                new_name += self._nome[i].upper()
            
            else:

                new_name += self._nome[i]
        
        return f"mostro: {new_name}"
    





def pariUguali(a: list[int], b: list[int]):

    c: list[int] = []

    if len(a) != len(b):

        raise ValueError("le liste devono avere la stessa lunghezza")
    
    for i in range(len(a)):

        if (a[i] % 2 == 0) and (b[i] % 2 == 0):

            c.append(1)
        
        else:

            c.append(0)
    
    return c




def combattimento(a: Alieno, m: Mostro):

    if (type(a) == Alieno) and (type(m) == Mostro):

        mylist = pariUguali(a.getMunizioni(), m.getAssalto())

        conta_valore = 0

        for i in range(len(mylist)):

            if mylist[i] == 1:

                conta_valore += 1
        
        if conta_valore > 4:

            for i in range(3 + 1):
                print(m.getVittoria())
            
            
        
        else:

            

            print(m.getSconfitta())
            
            
        

    else:

        print("il combattimento deve essere interrotto")

        return None 



def proclamaVincitore(c: Creatura):


    print("***********************"
    
    "*                           *" \
    "*                            *" \
    "*" \
    "    *************************")

    print(f"*************************"
        f"*                       *"
        f"*      {c.getNome()}    *"
        f"*                       *"
        )



    

    










    







        
    
    

    
    

        
