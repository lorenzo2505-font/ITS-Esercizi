from generi import *

class Noleggio:
    def __init__(self, film_list: list[Azione | Commedia | Drama]): # film_list sono i contenuti all'interno del negozio, rented_films sono i film noleggiati
        self.film_list = film_list
        self.rented_film: dict[int, list[Azione | Commedia | Drama]] = {}
    
    def isAvaible(self, film: Film):

        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")

            return True
        
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")

        return False
    
    def rentAMovie(self, film: Film, clientID: int):

        if clientID not in self.rented_film:
            self.rented_film[clientID] = []
        
        if film in self.rented_film[clientID]:
            raise ValueError('il cliente ha già noleggiato il film')
        
        if self.isAvaible(film):
            self.film_list.remove(film)
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
    
    def giveBack(self, film: Film, clientID: int, days: int):

             
        if clientID not in self.rented_film:
            raise ValueError('id cliente non registrato')

        if film not in self.rented_film[clientID]:
            raise ValueError('il cliente non ha noleggiato il film')
        
        if film in self.film_list:
            raise ValueError("il film è già presente all'interno del catalogo")
        
        self.rented_film[clientID].remove(film)
        self.film_list.append(film)

        if type(film) == Azione or type(film) == Commedia or type(film) == Drama:
            print(f'la penale da pagare per questo film è {film.calcolaPenaleRitardo(days)}')
        
        else:
            raise ValueError('il film deve avere un genere, non può essere generico')
    
    def printMovies(self):
        
        for i in self.film_list:
            print(f'{i.getTitle()}-{i.getGenere()}')

    def printRentedMovies(self, clientID: int):

        if clientID not in self.rented_film:
            raise KeyError('id cliente non registrato')

        for i in self.rented_film[clientID]:
            print(f'{i.getTitle()}-{i.getGenere()}')


if __name__ == '__main__':

    il_cavaliere_oscuro: Azione = Azione(1, 'il cavaliere oscuro')
    bullet_train: Azione = Azione(2, 'bullet train')
    kill_bill: Azione = Azione(3, 'kill bill')
    matrix: Azione = Azione(4, 'matrix')
    star_wars: Azione = Azione(5, 'star wars')

    fantozzi: Commedia = Commedia(6, 'fantozzi')
    i_simpson: Commedia = Commedia(7, 'i simpson')
    una_notte_da_leoni: Commedia = Commedia(8, 'una notte da leoni')
    deadpool: Commedia = Commedia(9, 'deadpool')

    il_miglio_verde: Drama = Drama(10, 'il miglio verde')

    catalogue: list = [il_cavaliere_oscuro, bullet_train, kill_bill, matrix, star_wars, fantozzi, i_simpson, una_notte_da_leoni, deadpool, il_miglio_verde]

    blockbuster_torva: Noleggio = Noleggio(catalogue)

    print("Quale film vuoi nolleggiare?")
    
    blockbuster_torva.rentAMovie(il_cavaliere_oscuro, 11)
    blockbuster_torva.rentAMovie(bullet_train, 11)

    blockbuster_torva.rentAMovie(bullet_train, 12)

    blockbuster_torva.rentAMovie(fantozzi, 12)

    blockbuster_torva.giveBack(fantozzi, 12, 1)

    blockbuster_torva.giveBack(bullet_train, 11, 2)

    blockbuster_torva.printMovies()



    
    
    

    
                

        
        


