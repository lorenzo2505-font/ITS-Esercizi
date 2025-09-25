class Pagamento:
    def __init__(self):
        self.__importo: float = 0.0
    
    def setImporto(self, importo: float):
        if importo < 0:
            raise ValueError("l'importo non può avere valore negativo")
        
        self.__importo = importo
    
    def getImporto(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self):
        print(f'importo del pagamento: €{round(self.getImporto(), 2)}')


if __name__ == '__main__':

    p: Pagamento = Pagamento()
    p.setImporto(20.0)
    p.dettagliPagamento()
    