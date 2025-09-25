from pagamento import Pagamento
from datetime import date

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, titolare: str, scadenza: date, numero: int):
        super().__init__()
        self.titolare = titolare 
        self.scadenza = scadenza
        self.numero = numero
    
    def dettagliPagamento(self):
        print(f"titolare: {self.titolare}, scadenza della carta: {self.scadenza.month}/{self.scadenza.year}, numero di carta: {self.numero} importo del pagamento: €{round(self.getImporto(), 2)}")


if __name__ == '__main__':
    
    p3: PagamentoCartaDiCredito = PagamentoCartaDiCredito('Mario Rossi', date(2024, 12, day = 1), 1234567890123456)
    p3.setImporto(200.0)
    p3.dettagliPagamento()

    p4: PagamentoCartaDiCredito = PagamentoCartaDiCredito('Luigi Bianchi', date(2025, 1, 1), 6543210987654321)
    p4.setImporto(500.0)
    p4.dettagliPagamento()


    