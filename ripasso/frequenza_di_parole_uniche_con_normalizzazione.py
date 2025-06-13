'''Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.

Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).

● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.

● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}'''


from string import punctuation





def count_unique_words(text: str):

    


    text = text.lower()



    mydict: dict = {}


    for i in text.split(" "):

        i = i.strip(punctuation)



        mydict[i] = text.count(i)
    
    
    return mydict
    
    



        
test = count_unique_words("Hello, world! Hello... PYTHON? world.")


print(test)



# versione prof



def countProf(text: str) -> dict[str, int]:

    text = text.lower()

    tokens: list[str] = text.split(" ")

    d: dict[str, int] = {}

    for token in tokens:

        token = token.strip(punctuation)

        if not token:

            continue

        if token not in d:

            d[token] = 1
        
        else:

            d[token] += 1






        