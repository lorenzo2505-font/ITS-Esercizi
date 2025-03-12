'''8-8. Album utente: inizia con il tuo programma dall'esercizio 8-7. 
Scrivi un ciclo while che consenta agli utenti di immettere l'artista e il titolo di un album.
 Una volta ottenute queste informazioni, chiama make_album() con l'input dell'utente e stampa il dizionario creato. 
 Assicurati di includere un valore quit nel ciclo while.'''

def make_album (artista: str, album: str, canzoni: int = None):
    return {"artista": artista, "album": album, "canzoni": canzoni}

while True:
    catch_artist = str(input("inserisci artista: "))
    catch_album = str(input("inserisci album: "))
    print(make_album(catch_artist, catch_album))
    break
