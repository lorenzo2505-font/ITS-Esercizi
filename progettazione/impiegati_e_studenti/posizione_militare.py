class PosizioneMilitare:

    _nome: str # noto alla nascita

    def __init__(self, nome: str):

        self.setNome(nome)
        
        

    def nome(self):

        return self._nome
    
    def setNome(self, nome: str):

        if (nome != "assolto") and (nome != "esente") and (nome != "dispensato"):

            raise ValueError("inserire una posizione valida")
        
        self._nome = nome
    
    def __str__(self):
        
        return f"{self._nome}"





