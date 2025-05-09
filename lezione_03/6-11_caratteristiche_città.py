'''6-11. Città: crea un dizionario chiamato città. Usa i nomi di tre città come chiavi nel tuo dizionario.
 Crea un dizionario di informazioni su ciascuna città e includi il paese in cui si trova la città, la sua popolazione approssimativa e un fatto su quella città. 
 Le chiavi per il dizionario di ogni città dovrebbero essere qualcosa come paese, popolazione e fatto. Stampa il nome di ogni città e tutte le informazioni che hai memorizzato su di essa.'''

città: dict = {"Roma": {
    "nazione": "Italia",
    "popolazione": 2700000,
    "fatto": "doppie file a donna olimpia"

},
"Firenze": {
    "nazione": "Italia",
    "popolazione": 300000,
    "fatto": "città con stile"
},
"Bari": {
    "nazione": "italia",
    "popolazione":  300000,
    "fatto": "si dice BERI"
}}



for key, value in città.items():
    print(key, value)