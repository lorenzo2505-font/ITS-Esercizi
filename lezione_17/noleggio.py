from generi import *

class Noleggi:
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

        if film not in self.film_list:
            raise ValueError('il film non è presente nel catalogo')
        
        if film in self.rented_film[clientID]:
            raise ValueError('il cliente ha già noleggiato il film')
        
        self.film_list.remove(film)

        if clientID not in self.rented_film:
            self.rented_film[clientID] = [film]
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
    
        
        else:
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
    
    def giveBack(self, film: Film, clientID: int, days: int):

        if film not in self.rented_film[clientID]:
            raise ValueError('il cliente non ha noleggiato il film')
        
        if film in self.film_list:
            raise ValueError("il film è già presente all'interno del catalogo")
        
        if clientID not in self.rented_film:
            raise ValueError('id non registrato')
        
        self.rented_film[clientID].remove(film)
        self.film_list.append(film)

        if type(film) == Azione or type(film) == Commedia or type(film) == Drama:
            print(f'la penale da pagare per questo film è {film.calcolaPenaleRitardo(days)}')
        
        else:
            raise ValueError()
    
    def printMovies(self):
        
        for i in self.film_list:
            print(f'{i.getTitle()}-{i.getGenere()}')

    def printRentedMovies(self, clientID: int):

        if clientID not in self.rented_film:
            raise KeyError('id non registrato')

        for i in self.rented_film[clientID]:
            print(f'{i.getTitle()}-{i.getGenere()}')


if __name__ == '__main__':

    il_cavaliere_oscuro: Azione = Azione(1, 'il cavaliere oscuro')
    fantozzi: Commedia = Commedia(2, 'fantozzi')
    popa_contro_tutti: Drama = Drama(3, 'popa contro tutti')

    blockbuster_torva: Noleggi = Noleggi([il_cavaliere_oscuro, fantozzi, popa_contro_tutti])

    blockbuster_torva.rentAMovie(il_cavaliere_oscuro, 1)
                

        
        


