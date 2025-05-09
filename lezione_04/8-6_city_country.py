'''8-6. Nomi delle città: scrivi una funzione chiamata city_country()
 che prenda il nome di una città e del suo paese. La funzione dovrebbe restituire una stringa formattata in questo modo:
   "Santiago, Cile". Chiama la tua funzione con almeno tre coppie città-paese e stampa i valori restituiti.'''

def city_country (città: str, paese: str):
    print(f"{città}, {paese}")

city_country ("Tokyo", "Giappone")
city_country ("Gotham City", "Stati Uniti")
city_country ("Madrid", "Spagna")
    