'''Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''




class FileManager:

    def __init__(self, nome_file, modalità):

        self.nome_file = nome_file

        self.modalità = modalità
    
    def __enter__ (self):

        self.file = open(self.nome_file, self.modalità)

        print("apertura del file")

        return self.file
    

    def __exit__(self, exc_type, exc_value, traceback):

        if self.file:

            self.file.close()

            print("chiusura del file")
        
        if exc_type is not None:

            print(f"exception type: {exc_type}")

            print(f"exception value: {exc_value}")

            print(f"traceback: {traceback}")
        
        return False




with FileManager ("lezione_15/lorem.txt", "w") as file:

    v = file.write("lorem ipsum")

    

    print(v)

with FileManager("lezione_15/lorem.txt", "r") as file_lettura:


    r = file_lettura.read()

    print(r)
        



    

    


    


    

    

    
    

    
    





        

        

        

            

        

        

    


        

        

        

        

        

        




    
    
    

