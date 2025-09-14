

def names():

    names: list[str] = [] # inizializzo la lista dei nomi vuota in cui andrò a inserire i nomi distinti
    string_m = None # inizializzo il valore del nome più lungo con None
    m = 0 # inizializzo il valore dei caratteri del nome più lungo a 0
    

    while True: # ciclo infinito
        name: str = str(input("inserisci nome: ")) # chiedo di inserire il nome in input

        if not(name) or len(name) > 20: # se il nome è una stringa vuota o ha più di 20 caratteri mando in errore il programma
            raise ValueError("il nome non deve essere vuoto e deve avere meno di 20 caratteri")
        
        if name not in names: # se il nome non fa parte della lista names allora non vi è una ripetizione quindi lo aggiungo alla lista e l'utente può continuare a inserire nomi
            names.append(name)
        
        elif name in names or len(names) == 30: # se invece il nome è nella lista names(si ha quindi una ripetizione) o la lista names ha lunghezza uguale a 30(quindi 30 nomi distinti) esco dal ciclo
            break
    
    for i in range(len(names)): # ciclo names

        if(len(names[i])) > m: # se la lunghezza del nome è maggiore di m allora string_m sarà uguale ad esso ed m sarà uguale al suo numero di caratteri
            string_m = names[i]
            m = len(names[i])
            
    
    print(f"hai inserito {len(names)} nomi distinti") # stampo il numero di nomi distinti usando la funzione len() su names
    print(f"il più lungo è {string_m} con {m} caratteri") # stampo il nome più lungo con i suoi caratteri


names()

