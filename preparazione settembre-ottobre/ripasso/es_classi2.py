class Movie: 

    def __init__(self, movie_id: str, title: str, director: str):

        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented: bool = False
    
    def rent(self):

        if self.is_rented:
            
            raise ValueError(f"{self.title} è già stato noleggiato")
        
        self.is_rented = True
    
    def return_movie(self):

        if not(self.is_rented):

            raise ValueError(f"{self.title} non è stato noleggiato da questo cliente")
        
        self.is_rented = False
    

class Customer:

    def __init__(self, customer_id: str, name: str):
        
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []
    
    def rent_movie(self, movie: Movie):

        if movie.is_rented:

            raise ValueError(f"{movie.title} è già stato noleggiato")
        
        self.rented_movies.append(movie)
        movie.rent()
    
    def return_movie(self, movie: Movie):

        if movie not in self.rented_movies:

            raise ValueError(f"{movie.title} non è nella sua lista")
        
        if not(movie.is_rented):

            raise ValueError(f"{movie.title} non è mai stato noleggiato")
        
        self.rented_movies.remove(movie)
        movie.return_movie()

class VideoRentalStore:

    def __init__(self):

        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}
    
    def add_movie(self, movie_id: str, title: str, director: str):

        if movie_id in self.movies:
            
            raise ValueError(f"{title} è già presente nell'elenco")
        
        self.movies[movie_id] = Movie(movie_id, title, director)
    
    def register_customer(self, customer_id: str, name: str):

        if customer_id in self.customers:

            raise ValueError(f"{name} è già registrato")
        
        self.customers[customer_id] = Customer(customer_id, name)
    
    def rent_movie(self, customer_id: str, movie_id: str):

        if (customer_id not in self.customers) or (movie_id not in self.movies):

            raise ValueError("film o utente non trovato")
        
        self.customers[customer_id].rent_movie(self.movies[movie_id])
    
    def return_movie(self, customer_id: str, movie_id: str):

        
        if (customer_id not in self.customers) or (movie_id not in self.movies):

            raise ValueError("film o utente non trovato")
        
        self.customers[customer_id].return_movie(self.movies[movie_id])
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id not in self.customers:
            
            raise ValueError(f"utente non trovato {[]}")
        
        return self.customers[customer_id].rented_movies



def main():

    il_cavaliere_oscuro: Movie = Movie("1", "il cavaliere oscuro", "cristopher nolan")
    #il_cavaliere_oscuro.rent()
    #il_cavaliere_oscuro.return_movie()

    popa: Customer = Customer("2", "alessandro popa")
    #popa.rent_movie(il_cavaliere_oscuro)
    #popa.return_movie(il_cavaliere_oscuro)

    blockbuster_torvaianica: VideoRentalStore = VideoRentalStore()
    blockbuster_torvaianica.add_movie(il_cavaliere_oscuro.movie_id, il_cavaliere_oscuro.title, il_cavaliere_oscuro.director)
    blockbuster_torvaianica.register_customer(popa.customer_id, popa.name)
    blockbuster_torvaianica.rent_movie(popa.customer_id, il_cavaliere_oscuro.movie_id)
    #blockbuster_torvaianica.return_movie(popa.customer_id, il_cavaliere_oscuro.movie_id)
    print(blockbuster_torvaianica.get_rented_movies(popa.customer_id))




main()
    
    
    
    


        

        
        
    
            

            

        