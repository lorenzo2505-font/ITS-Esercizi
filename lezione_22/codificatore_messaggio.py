from abc import ABC, abstractmethod

from string import ascii_lowercase, ascii_uppercase



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

        self.setChiave(chiave)
    
    def setChiave(self, chiave: int):

        if chiave < 0:

            raise ValueError("la chiave non può avere un valore negativo")
        
        if chiave > 26:

            while chiave > 26:

                chiave -= 26
        
        self.chiave = chiave


        
    def codifica(self, testoInChiaro: str) -> str:
        
        l = ascii_lowercase
        u = ascii_uppercase

        messaggio_codificato: str = ""

        


        for i in range(len(testoInChiaro)):

            if testoInChiaro[i] in l:

                for j in range(len(l)):

                    if l[j] == testoInChiaro[i]:

                        messaggio_codificato += l[j + self.chiave]

            elif testoInChiaro[i] in u:

                for j in range(len(u)):

                    if u[j] == testoInChiaro[i]:

                        messaggio_codificato += u[j + self.chiave]
            else:

                messaggio_codificato += testoInChiaro[i]
        
        return messaggio_codificato
    

    
    
    def decodifica(self, testoCodificato: str) -> str:
        
        l = ascii_lowercase
        u = ascii_uppercase

        messaggio_decodificato: str = ""

        for i in range(len(testoCodificato)):

            if testoCodificato[i] in l:

                for j in range(len(l)):

                    if l[j] == testoCodificato[i]:

                        messaggio_decodificato += l[j - self.chiave]
            
            elif testoCodificato[i] in u:

                for j in range(len(u)):

                    if u[j] == testoCodificato[i]:

                        messaggio_decodificato += u[j - self.chiave]
            
            else:

                messaggio_decodificato += testoCodificato[i]
        
        return messaggio_decodificato
    
    def file(self):

        with open("lezione_22/myfile.txt", "r") as file:

            testo = file.read()
        
        c = self.codifica(testo)

        with open("lezione_22/encrypt_file.txt", "w") as file2:

            file2.write(c)
        
        with open("lezione_22/encrypt_file.txt", "r") as file3:

            testo_codificato = file3.read()
        
        return testo_codificato

            
        
        

            
        

        




class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int):
        super().__init__()

        self.n = abs(n)
    
    def codifica(self, testoInChiaro: str) -> str:

        messaggio_codificato: str = ""


        for x in range(self.n):
        
            if len(testoInChiaro) % 2 != 0:

                s1 = testoInChiaro[0: int(len(testoInChiaro) / 2 + 1)]
                
                s2 = testoInChiaro[int(len(testoInChiaro) / 2 + 1):]

            else:

                s1 = testoInChiaro[0: int(len(testoInChiaro) / 2)]
                
                s2 = testoInChiaro[int(len(testoInChiaro) / 2):]
            
            
            for i in range(len(s1)):

                try: # aggiungo a turno un carattere delle due stringhe (ciclo la prima perché se la lunghezza è dispari è la più lunga)

                    messaggio_codificato += s1[i]
                    messaggio_codificato += s2[i]
                
                except IndexError: # se vi è un IndexError sulla seconda stringa (che capiterà se la lunghezza del testo è dispari) quest'ultimo viene ignorato e non verrà alazata l'eccezione
                    pass
        
        return messaggio_codificato



            
        
        

    def decodifica(self, testoCodificato: str) -> str:

        group1: str = ""

        group2: str = ""

        messaggio_decodificato: str = ""

        for i in range(len(testoCodificato)):

            if i % 2 == 0:

                group1 += testoCodificato[i]
            
            else:

                group2 += testoCodificato[i]
        
        messaggio_decodificato += group1 + group2

        return messaggio_decodificato
    
    def file(self):

        with open("lezione_22/meteora.txt", "r") as file:

            testo = file.read()
        
        c = self.codifica(testo)

        with open("lezione_22/encrypt_file.txt", "w") as file2:

            file2.write(c)
        
        with open("lezione_22/encrypt_file.txt", "r") as file3:

            testo_codificato = file3.read()
        
        return testo_codificato
        







def main():


    '''c: CifratoreAScorrimento = CifratoreAScorrimento(3)

    print(c.codifica("aA!"))
    print(c.decodifica("dD!"))

    c2: CifratoreACombinazione = CifratoreACombinazione(1)

    print(c2.codifica("abcdefghi"))
    print(c2.decodifica("afbgchdie"))'''

    numb: CifratoreAScorrimento = CifratoreAScorrimento(3)

    print(numb.file())

    faint: CifratoreACombinazione = CifratoreACombinazione(1)

    print(faint.file())

    


    


main()
        

        

        
