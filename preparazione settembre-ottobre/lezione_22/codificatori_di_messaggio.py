from abc import ABC, abstractmethod
from string import ascii_lowercase
from string import ascii_uppercase

class CodificatoreMessaggio(ABC):

    @abstractmethod

    def codifica(self, testoInChiaro: str):
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod

    def decodifica(self, testoCodificato: str):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int):
        super().__init__()

        self.chiave = chiave
    
    def codifica(self, testoInChiaro: str):
        
        encriptato: str = ""
        l = ascii_lowercase
        u = ascii_uppercase

        while self.chiave > 26:
            self.chiave -= 26
        
        for i in range(len(testoInChiaro)):

            if testoInChiaro[i] in l:

                for j in range(len(l)):

                    if l[j] == testoInChiaro[i]:
                        encriptato += l[(j + self.chiave) % len(l)]

            elif testoInChiaro[i] in u:

                for j in range(len(u)):

                    if u[j] == testoInChiaro[i]:
                        encriptato += u[(j + self.chiave) % len(u)]
            
            else:
                encriptato += testoInChiaro[i]
        
        return encriptato
    
    def decodifica(self, testoCodificato):

        decriptato: str = ""
        l = ascii_lowercase
        u = ascii_uppercase

        while self.chiave > 26:
            self.chiave -= 26
        
        for i in range(len(testoCodificato)):

            if testoCodificato[i] in l:

                for j in range(len(l)):

                    if l[j] == testoCodificato[i]:
                        decriptato += l[j - self.chiave]

            elif testoCodificato[i] in u:

                for j in range(len(u)):

                    if u[j] == testoCodificato[i]:
                        decriptato += u[j - self.chiave]
            
            else:
                decriptato += testoCodificato[i]
        
        return decriptato
    
    def leggi_da_file(self):
        
        with open("lezione_22/testo_chiaro.txt", "r") as f:
            testoInChiaro = f.read()
        
        return testoInChiaro
    
    def scrivi_su_file(self, testoInChiaro: str):

        with open("lezione_22/testo_da_cifrare.txt", "w") as f:
            t = f.write(testoInChiaro)
        
        return t

        


class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int):
        super().__init__()

        self.n = n
    
    def codifica(self, testoInChiaro: str):

        encriptato: str = ""
        first_leg: str = ""
        second_leg: str = ""

        if len(testoInChiaro) % 2 == 0:
            first_leg += testoInChiaro[:int(len(testoInChiaro) / 2)]
            second_leg += testoInChiaro[int(len(testoInChiaro) / 2): ]
        
        else:
            first_leg += testoInChiaro[:int(len(testoInChiaro) / 2 + 1)]
            second_leg += testoInChiaro[int(len(testoInChiaro) / 2 + 1): ]
        
        for volte in range(self.n):

            for i in range(len(second_leg)):
                encriptato += first_leg[i]
                encriptato += second_leg[i]
            
            if len(first_leg) > len(second_leg):
                encriptato += first_leg[-1]
        
        return encriptato


        
        
    
    def decodifica(self, testoCodificato):
        
        first_leg: str = ""
        second_leg: str = ""
        decriptato: str = ""

        for i in range(len(testoCodificato)):
            
            if i % 2 == 0:
                first_leg += testoCodificato[i]
            
            else:
                second_leg += testoCodificato[i]
        
        decriptato += first_leg + second_leg

        return decriptato
    
      
    def leggi_da_file(self):
        
        with open("lezione_22/testo_chiaro.txt", "r") as f:
            testoInChiaro = f.read()
        
        return testoInChiaro
    
    def scrivi_su_file(self, testoCodificato: str):

        with open("lezione_22/testo_cod.txt", "w") as f:
            t = f.write(testoCodificato)
        
        
    



def main():

    scorrimento: CifratoreAScorrimento = CifratoreAScorrimento(3)
    ls = scorrimento.leggi_da_file()
    #print(ls)
    cod_s = scorrimento.codifica(ls)
    scorrimento.scrivi_su_file(cod_s)
    print(cod_s)
    decod_s = scorrimento.decodifica(cod_s)
    print(decod_s)

    combinazione: CifratoreACombinazione = CifratoreACombinazione(3)
    lc = combinazione.leggi_da_file()
    #print(lc)
    cod_c = combinazione.codifica(lc)
    combinazione.scrivi_su_file(cod_c)
    print(cod_c)
    decod_c = combinazione.decodifica(cod_c)
    print(decod_c)


main()
        
