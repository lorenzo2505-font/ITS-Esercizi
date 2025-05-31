from custom_types import *

class Città:

    _nome: str # noto alla nascita

    _abitanti: int # noto alla nascita


    def __init__(self, nome: str, abitanti: int):
        


        self.setNome(nome)

        self.setAbitanti(abitanti)
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    
    def setAbitanti(self, abitanti: int):

        if abitanti >= 0:

            self._abitanti = abitanti
        
        else:

            raise ValueError("il numero di abitanti non può essere negativo")
    

    def nome(self):

        return self._nome
    
    def abitanti(self):

        return self._abitanti
    
    def __str__(self):
        
        return f"nome città: {self._nome}, abitanti: {self._abitanti}"


class Compagnia:

    _nome: str # noto alla nascita 

    _anno: int # <<immutable>> noto alla nascita

    _città: Città # noto alla nascita

    
    def __init__(self, nome: str, anno: int, città: Città):
        
        self.setNome(nome)

        if anno > 1900:

            self._anno = anno
        
        else:

            ValueError ("inserire un anno di fondazione prima del 1900")
        
        self.setCittà(città)
    

    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            ValueError("inserire un nome valido")
    
    def setCittà(self, città: Città):

        self._città = città
    
    def nome(self):

        return self._nome
    
    def anno(self):

        return self._anno
    
    def città(self):

        return self._città
    
    def __str__(self):
        
        return f"nome compagnia: {self._nome}, anno di fondazione: {self._anno}, città: {self._città}"




















class Volo:

    _durata_min: int # noto alla nascita

    _codice: CodiceVolo # <<immutable>>, noto alla nascita

    _compagnia: Compagnia # <<immutable>>, noto alla nascita

    


    def __init__(self, durata_min: int, codice: CodiceVolo, compagnia: Compagnia):
        

        self.setDurata(durata_min)

        self._codice = codice

        self._compagnia = compagnia
    
    def setDurata(self, durata_min: int):

        if durata_min <= 0:

            raise ValueError("non ci possono essere durate di voli con valore minore o uguale a zero")
        
        else:

            self._durata = durata_min
    
    def durata(self):

        return self._durata
    
    def codice(self):

        return self._codice
    
    def compagnia(self):

        return self._compagnia
    
    def __str__(self):
        
        return f"durata volo: {self._durata} minuti, codice: {self._codice}, compagnia: {self._compagnia}"


c: CodiceVolo = CodiceVolo("AZ123")

volo: Volo = Volo(60, c)

#print(v)




    

compagnia: Compagnia = Compagnia("pierlions flights", 1998)

#print(c)






città: Città = Città("roma", 3000000)

#print(città)



class Nazione:

    _nome: str # noto alla nascita

    def __init__(self, nome: str):
        
        self.setNome(nome)
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            ValueError("inserire un nome valido")
    

    def nome(self):

        return self._nome
    
    def __str__(self):
        
        return f"nome nazione: {self._nome}"
    

nazione: Nazione = Nazione ("italia")

#print(nazione)


class Aereoporto:

    _nome: str # noto alla nascita

    _codice: CodiceAereoporto # <<immutable>> noto alla nascita


    def __init__(self, nome: str, codice: CodiceAereoporto):
        
        self.setNome(nome)

        self._codice = codice
    

    def setNome(self, nome: str):

        
        if nome:

            self._nome = nome
        
        else:

            raise ValueError("inserire un nome valido")
    

    def nome(self):

        return self._nome
    
    def codice(self):

        return self._codice
    
    def __str__(self):

        return f"nome aereoporto: {self._nome}, codice: {self._codice}"


aereoporto: Aereoporto = Aereoporto ("aereoporto di fiumicino", "FCO")

#print(aereoporto)




        





        
