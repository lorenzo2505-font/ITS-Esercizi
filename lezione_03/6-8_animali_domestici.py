'''6-8. Animali domestici: crea diversi dizionari, in cui ciascun dizionario rappresenta un animale domestico diverso. In ogni dizionario indicare la specie dell’animale e il nome del proprietario. 
Conserva questi dizionari in un elenco chiamato animali domestici. Quindi, scorri l'elenco e as
lo fai, stampa tutto quello che sai su ciascun animale domestico.'''

pet1: dict  = {"animale": "gatto",  "propietario": "Lorenzo"}

pet2: dict = {"animale": "cane", "propietario": "Matteo"}

pet3: dict = {"animale": "scimmia", "propietario": "Re Kaioh"}

animali_domestici: list = [pet1, pet2, pet3]

for i in range(len(animali_domestici)):
    print(animali_domestici[i])
   
    
