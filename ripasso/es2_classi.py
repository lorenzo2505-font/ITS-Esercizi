'''Progettare un sistema di videonoleggio con i seguenti requisiti:
1. Classe Movie:
Attributi:
● movie_id: str - Identificatore di un film.
● title: str - Titolo del film.
● director: str - Regista del film.
● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

Metodi:
● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
film '{self.title}' è già noleggiato."
● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
stato noleggiato da questo cliente."



2. Classe Customer:

Attributi:
● customer_id: str - Identificativo del cliente.
● name: str - Nome del cliente.
● rented_movies: list[Movie] - Lista dei film noleggiati.

Metodi:
● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
noleggiato."
● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
noleggiato da questo cliente."



3. Classe VideoRentalStore:

Attributi:
● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
l'oggetto Movie.
● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
valore l'oggetto Customer.


Metodi:
● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
ID '{movie_id}' esiste già."

● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
con ID '{customer_id}' è già registrato."

● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."

● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."

● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.



'''





class Movie:

    def __init__(self, movie_id: str, title: str, director: str):
        
        self.id = movie_id

        self.title = title

        self.director = director

        self.is_rented: bool = False
    

    def rent(self):

        if self.is_rented == False:

            self.is_rented = True

            print("film noleggiato")
        
        else:

            raise Exception("Il film è già stato noleggiato")
    
    def return_movie(self):

        if self.is_rented == True:

            self.is_rented = False

            print("film restituito")
        
        else:

            raise Exception("il film non è stato noleggiato da questo cliente")
    
    def __str__(self):
        
        return f"film: {self.title}, regista: {self.director}"
    
    
    


class Customer:


    def __init__(self, customer_id: str, name: str):


        self.id = customer_id

        self.name = name

        self.rented_movies: list[Movie] = []
    

    def rent_movie(self, movie: Movie):

        if movie.is_rented == False:

            self.rented_movies.append(movie)

            movie.is_rented = True

            print("film noleggiato")
        

        else:

            raise Exception("il film è già stato noleggiato")
    

    def return_movie(self, movie: Movie):

        if movie.is_rented == True:

            self.rented_movies.remove(movie)

            movie.is_rented = False

            print("film restituito")
        
        else:

            raise Exception("Il film non è stato noleggiato da questo cliente")







class VideoRentalStore:



    def __init__(self):
        

        self.movies: dict[str, Movie] = {}

        self.customers: dict[str, Customer] = {}

    
    def add_movie(self, movie_id: str, title: str, director: str):



        if movie_id in self.movies.keys():

            raise Exception("Il film è già presente")
        
        else:

            self.movies[movie_id] = Movie(movie_id, title, director)

            print("film aggiunto con successo")
    

    def register_customer(self, customer_id: str, name: str):



        if customer_id in self.customers.keys():

            raise Exception("già registrato")
        
        else:

            self.customers[customer_id] = Customer(customer_id, name)

            print("utente registrato")
    

    def rent_movie(self, customer_id: str, movie_id: str):


        if customer_id not in self.customers.keys():

            raise Exception("il membro non è registrato")
        
        if movie_id not in self.movies.keys():

            raise Exception("il film non è presente nel negozio")
        
        self.customers[customer_id].rent_movie(self.movies[movie_id])

    
    def return_movie(self, customer_id: str, movie_id: str):


        if customer_id not in self.customers.keys():

            raise Exception("il membro non è necessario")
        
        if movie_id not in self.movies.keys():

            raise Exception("il film non è presente nel nostro negozio")
        
        self.customers[customer_id].return_movie(self.movies[movie_id])
    

    def get_rented_movies(self, customer_id: str) -> list[Movie]:


        if customer_id not in self.customers.keys():

            raise Exception("Il membro non è registrato")
        

        movieList: list[Movie] = self.customers[customer_id].rented_movies

        return movieList
    
    def all_movies(self):

        for value in self.customers.values():

            return value.rented_movies

            

            

            
        

        




m: Movie = Movie("1234", "bolli pallone d'oro", "andrea d'ippoliti")


m.rent()


m.return_movie()


c: Customer = Customer("5678", "lorenzo acomanni")


c.rent_movie(m)

c.return_movie(m)


v: VideoRentalStore = VideoRentalStore()


v.add_movie("1111", "il cavaliere oscuro", "nolan")


v.register_customer("5555", "massimiliano termine")


v.rent_movie("5555", "1111")


print(v.all_movies())


#v.return_movie("5555","1111")


print(v.get_rented_movies("5555"))









    

            
        

        


        

    


    

        

    
    
