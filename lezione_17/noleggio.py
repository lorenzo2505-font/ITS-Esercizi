from generi import *

class Noleggi:
    def __init__(self, film_list: list[Film]): # film_list sono i contenuti all'interno del negozio, rented_films sono i film noleggiati
        self.film_list = film_list
        self.rented_film: dict[int, list[Film]]
    
    def isAvaible(self, film: Film):

        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")

            return True
        
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")

        return False
    
    def rentAMovie(self, film: Film, clientID: int):
        pass


