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
    
    def decodifica(self, testoCodificato):
        return super().decodifica(testoCodificato)




class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int):
        super().__init__()

        self.n = abs(n)
    
    def codifica(self, testoInChiaro):

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



            
        
        

                

                
        

        
        
        
        
    
    
    def decodifica(self, testoCodificato):
        return super().decodifica(testoCodificato)







def main():


    '''c: CifratoreAScorrimento = CifratoreAScorrimento(3)

    print(c.codifica("aA!"))'''

    c2: CifratoreACombinazione = CifratoreACombinazione(1)

    print(c2.codifica("abcdefghi"))


main()
        

        

        
