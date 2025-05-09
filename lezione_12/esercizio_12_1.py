'''Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste,
      viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore 
    se nessun film contiene la parola cercata nel titolo.
 
Codice driver

    Crea un’istanza della classe MovieCatalog.
    Aggiungi nuovi film e registi.
    Aggiungi film a registi già presenti nel catalogo.
    Rimuovi film dal catalogo.
    Elenca i registi presenti nel catalogo.
    Visualizza film di uno specifico regista.
    Cerca film per parola chiave nel titolo, gestendo il caso con risultati che senza.

'''

class MovieCatalog:
    '''
    attributi della classe MovieCatalog:
    self.catalog: dict [str, list[str]]
    '''

    #inizializzare un oggetto della classe MovieCatalog

    def __init__(self):
        self.setCatalog()
    
    #metodi setter

    #metodo che imposta il valore dell'attributo self.catalog

    def setCatalog (self) -> None:
        self.catalog: dict[str, list[str]] = {}
    
    #metodo getter

    #metodo che ritorna il valore del dell'attributo self.catalog

    def getCatalog (self) -> dict[str, list[str]]:
        return self.catalog
    
    #metodi della classe MovieCatalog

    #metodo che aggiunge una lista di film al cadalogo

    def add_movie(self, director_name: str, movies: list[str]) -> None:
        #check valore valido di director_name
        if not director_name:
            print("fornire un nome valido per il regista")
        
        elif not movies:
            print("fornire una lista di film che non sia vuota")
        
        #se i dati inseriti sono validi:

        else:
            if director_name in self.catalog:
                #aggiungere film al catalogo
                for movie in movies:
                    if movie in self.catalog[director_name]:
                        print(f"il film movie è già presente nel catalogo")
                    else:
                        #aggiunta del film
                        self.catalog[director_name].append(movie)

             #se il regista non è nel catalogo
            else:
                self.catalog[director_name] = movies

    def remove_movie (self, director_name: str, movie_name):
        if not director_name:
            print("fornire un nome valido")

        elif not movie_name:
            print("fornire un film valido")
        
        else:
            if director_name in self.catalog and movie_name in self.catalog[director_name]:

                self.catalog[director_name].remove(movie_name)
            
            if not self.catalog[director_name]:
                #rimuovere il regista dal catalogo
                del self.catalog[director_name]

    def list_directors(self) ->list[str]:
        return list(self.catalog.keys())
    
    def get_movies_by_director (self, director_name: str) -> list[str]:
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return "errore, il regista o non esiste, o non è presente nel nostro catalogo"
    
    def search_movies_by_title(self, title: str):
        #new_dict: dict[str, list[str]] = {}
        #mylist: list = []

        for key, value in self.catalog.items():
                
            if title in value:
                return key, value
            else:
                return "errore, il titolo che cerchi o non esiste o non è nel nostro catalogo"
        
        
        


                

                
        
       
            

            
        



        
    


        


      
    




    