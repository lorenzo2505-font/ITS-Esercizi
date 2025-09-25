from pagamento import Pagamento

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()
    
    def dettagliPagamento(self):
        print(f'importo del pagamento in contanti: €{round(self.getImporto(), 2)}')
    
    def inPezziDa(self):
        n = self.getImporto()
        banconote: list = [500, 200, 100, 50, 20, 10, 5, 1, 0.5, 0.2, 0.1, 0.05, 0.01 ]
        mydict: dict[int, int] = {}

        for i in range(len(banconote)):

            while n - banconote[i] >= 0:
                
                if banconote[i] not in mydict:
                    mydict[banconote[i]] = 1
                
                else:
                    mydict[banconote[i]] += 1
                
                n -= banconote[i]
                n = round(n, 2)
            
            if n == 0:
                break

        for key, value in mydict.items():
            print(f'numero di pezzi da {key} euro: {value}')
            
        
        
        
        



if __name__ == '__main__':

    p1: PagamentoContanti = PagamentoContanti()
    p1.setImporto(150.0)
    p1.inPezziDa()

    p2: PagamentoContanti = PagamentoContanti()
    p2.setImporto(95.25)
    p2.inPezziDa()


    
