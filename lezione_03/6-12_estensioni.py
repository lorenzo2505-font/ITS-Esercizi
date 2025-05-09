'''6-12. Estensioni: ora stiamo lavorando con esempi abbastanza complessi da poter essere estesi in molti modi.
 Utilizzare uno dei programmi di esempio di questo capitolo ed estenderlo aggiungendo nuove chiavi e valori, 
 modificando il contesto del programma o migliorando la formattazione dell'output.'''

favorite_places: dict = {"Lorenzo": "Roma", "Gianluca": "Firenze", "Andrea": "Cassino"}

favorite_places["Francesco"] = "Bari"
favorite_places["Luca"] = "Ischia"

for key, value in favorite_places.items():
    print(key, value)
