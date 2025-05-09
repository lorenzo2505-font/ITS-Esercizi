'''Scrivi una funzione che, data una lista, 
ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.'''

def frequency_dict(elements: list) -> dict:
    mydict: dict = {}
    for i in elements:
        elements.count(i)
        mydict[i] = elements.count(i)
    return mydict

print(frequency_dict(['mela', 'banana', 'mela']))

