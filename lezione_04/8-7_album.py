'''8-7. Album: scrivi una funzione chiamata make_album() che costruisca un dizionario che descriva un album musicale.
 La funzione dovrebbe accettare un nome di artista e un titolo di album e dovrebbe restituire un dizionario contenente queste due informazioni. 
 Usa la funzione per creare tre dizionari che rappresentano album diversi. 
 Stampa ogni valore restituito per mostrare che i dizionari stanno memorizzando correttamente le informazioni dell'album.
   Usa None per aggiungere un parametro facoltativo a make_album() che ti consente di memorizzare il numero di brani in un album.
 Se la riga di chiamata include un valore per il numero di brani, 
 aggiungi quel valore al dizionario dell'album. Crea almeno una nuova chiamata di funzione che includa il numero di brani in un album.'''

def make_album (artista: str, album: str, canzoni: int = None):
    if canzoni == None or canzoni < 0:
        return {"artista": artista, "album": album}
    else:
        return {"artista": artista, "album": album, "canzoni": canzoni}

catch_dict1 = make_album ("linkin park", "hybrid theory", 12)
print(catch_dict1)

catch_dict2 = make_album ("the score", "pressure")
print(catch_dict2)

catch_dict3 = make_album ("eminem", "the eminem show")
print(catch_dict3)
