from esercizio_12_1 import MovieCatalog

#creare un oggetto della classe MovieCatalog

catalog: MovieCatalog = MovieCatalog()

#aggiungiamo un regista e dei film al catalogo 

catalog.add_movie ("Steven Spielberg", ["Casper", "Jurassic Park"])

print(catalog.getCatalog())

#aggiungere un altro film di spielberg al catalogo

catalog.add_movie("Steven Spielberg", ["ET"])

print(catalog.getCatalog())

catalog.remove_movie("Steven Spielberg", "ET")

print(catalog.getCatalog())

#print(catalog.list_directors())

'''catalog.add_movie("Cristopher Nolan", ["The Prestige", "Il Cavaliere Oscuro", "Dunkirk"])



print(catalog.get_movies_by_director("Cristopher Nolan"))

#print(catalog.search_movies_by_title("oscuro"))'''

print(catalog.search_movies_by_title("Jurassic Park"))




