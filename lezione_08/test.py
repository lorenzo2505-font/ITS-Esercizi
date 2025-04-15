from lezione_ereditarietà import Persona

from studente import Studente

#creo un oggetto della classe persona +
fm: Persona = Persona ("Federico", "March", 29)

print(fm)

#creo un oggetto della classse studente 
studente1: Studente = Studente("Mario", "Rossi", "0123456")


#visualizzare 

print(studente1)

#controlllo se studente1 fa parte della classe Studente

#isistance (obj, Class) -> controlla se l'oggetto obj sia un'istanza della classe Class

#in caso affermativo -> True

#in caso negativo -> False

#controllo se studente1 è istanza della classe Studente
if isinstance (studente1, Studente):
    print("studente è istanza della classe Studente")


#controllo se studente1 è istanza della classe Persona
if isinstance (studente1, Persona):
    print("studente è istanza della classe Persona")


#controllo se fm è istanza della classe Persona

if isinstance (fm, Persona):
    print("fm è istanza della classe Persona")


#controllo se fm è istanza della classe Studente

if isinstance(fm, Studente):
    print("fm è sia Persona che Studente")

else:
    print("fm è sia Persona ma NON è Studente")


#controllare che la classe Studente si sottoclasse di Persona 

#issubclass (Class1, Class2) -> controlla se Class1 sia sottoclasse di Class2

if issubclass (Studente, Persona):
    print("Studente è sottoclasse di Persona")






