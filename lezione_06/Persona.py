class Persona:
    '''
    di una persona si devono sapere delle informazioni.
    queste informazioni vengono chiamate attributi della classe Persona
    queste informazioni possono essere:
    
    -nome
    -cognome
    -età
    
    come verranno rappresentati in Python ?
    self.name: str (attributo di tipo stringa)
    self.lastname: str (attributo di tipo stringa)
    self.age: int (attributo di tipo intero) '''

    #costruttore delle classe persona 

    def __init__(self, name: str, lastname: str, age: int):
        self.name = name #tutti questi attributi si riferiscono alla classe persona con self
        self.lastname = lastname
        self.age = age

    #funzione che mostri in ouput tutti i dati di una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")


l: Persona = Persona ("Lorenzo", "Acomanni", 19)

print(l)

#mostra dati di una persona 

l.displayData ()


