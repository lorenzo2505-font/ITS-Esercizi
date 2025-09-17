class Regione:
    _nome: str # noto alla nascita

    def __init__(self, nome: str):
        self.setNome(nome)
    
    def setNome(self, nome: str):
        
        if nome:
            self._nome = nome
        
        else:
            raise ValueError('inserire un nome valido')
    
    def getNome(self) -> str:
        return self._nome
    
    def __str__(self):
        return f'nome regione: {self._nome}'


if __name__ == '__main__':

    lazio: Regione = Regione('Lazio')
    print(lazio)