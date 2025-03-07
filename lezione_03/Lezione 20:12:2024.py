#sintassi: modo in cui si scrivono le cose 
#semantica: cosa vogliono dire quelle cose 
#lista_1= [i for i in range(10)]
#for numero in lista_1: 
    #print(numero)
    #lista_2=["a", "b", "c"]
    #for lettera in lista_2:
       #print(lettera)

lista1=[1, 2, 3]
lista2=["a", "b", "c"]
L= [[("a", 1), ("a", 2), ("a", 3)],
[("b", 1), ("b", 2), ("b", 3)],
[("c", 1), ("c",2), ("c", 3)]]
for i in range(3):
    for j in range(3): #qui si è  usata l'indicizzazione 
        if(L[i][j][1]%2)==0: #con 1 mi specifica quel specifico indice
            print(L[i] [j])


listaNum=[1, 2, 3]
for num in listaNum:
  if num%2==0:
   print(num)












