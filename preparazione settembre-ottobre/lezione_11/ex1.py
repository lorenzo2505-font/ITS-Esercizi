class Film:

    def __init__(self, titolo: str, durata: int):
        
        self.titolo = titolo
        self.durata = durata

class Sala:

    def __init__(self, numero: int, film: Film, posti: int):
        
        self.numero = numero
        self.film = film
        self.posti = posti
        self.posti_prenotati = 0
    
    def prenota_posti(self, num_posti: int):

        if num_posti > self.posti:
            
            raise ValueError("posti non disponibili")
        
        self.posti_prenotati += num_posti
        self.posti -= self.posti_prenotati
    
    def posti_disponibili(self):

        return self.posti


class Cinema:

    def __init__(self):
        
        self.sale: list[Sala] = []
    
    def aggiungi_sala(self, sala: Sala):

        if sala in self.sale:

            raise ValueError("la sala è già presente nell'elenco")
        
        for i in self.sale:
            
            if i.numero == sala.numero:

                raise ValueError("due sale non possono avere lo stesso numero")
        
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film: str, num_posti: int):

        for i in self.sale:
            
            if i.film.titolo == titolo_film:
                
                i.prenota_posti(num_posti)
                
                return "film prenotato"
        
        return "il film non è presente nel nostro cinema"
    

def main():

    il_cavaliere_oscuro: Film = Film("il cavaliere oscuro", 150)

    sala1: Sala = Sala(1, il_cavaliere_oscuro, 100)

    cinema_its: Cinema = Cinema()
    cinema_its.aggiungi_sala(sala1)
    print(cinema_its.prenota_film("il cavaliere oscuro", 4))

main()


    

    
    