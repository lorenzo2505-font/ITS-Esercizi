'''6-9. Luoghi preferiti: crea un dizionario chiamato favorite_places.
 Pensa a tre nomi da utilizzare come chiavi nel dizionario e memorizza da uno a tre luoghi preferiti per ogni persona. 
 Per rendere questo esercizio un po' più interessante, chiedi ad alcuni amici di nominare alcuni dei loro posti preferiti. 
 Sfoglia il dizionario e stampa il nome di ogni persona e i suoi luoghi preferiti.'''

favorite_places: dict = {"Lorenzo": "Roma", "Gianluca": "Firenze", "Andrea": "Cassino"}

for key, value in favorite_places.items():
    print(key,value)