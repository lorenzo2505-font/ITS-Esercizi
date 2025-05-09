from speak import Persona

from alieno import Alieno

#creare un oggetto p della classe persona 

p: Persona = Persona ("Lorenzo", "Acomanni", 20)

print(p)

#creare un oggetto et della classe alieno 

et: Alieno = Alieno("Andromeda")

#visualizzare le informazioni dell'oggetto et

print("\n", et)

#invocare il metodo speak della classe Persona 

p.speak()

#invocare il metodo speak della classe alieno 

et.speak()
