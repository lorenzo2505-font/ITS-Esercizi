#Formattazione delle stringhe ed escape characters ed altro
name:  str="Federico"
age: int=9
#concatenazione di stringhe 
print(type(age)) #da int
print(type(str(age))) #da stringa
age= str(age)
print(type(age)) 
#output formattato
print(f"ciao io sono {name} ho {age} anni")
pi: float=3.14159265359
print(f"pi greco vale {pi}")
#scrivere pi greco con due decimali
print(f"pi greco vale: {pi:.2f}")
#scrivere p greco con 3 decimali
print(f"pi greco vale: {pi:.3f}") #si arrontonda anche 
#caratteri escape 
print(f"ciao, io sono {name}\n ho {age} anni") #newline, fa andare a capo 
print("c.documents//folder//img.png") #fa vedere le sbarre 
print(" ciao \t bla...bla")
