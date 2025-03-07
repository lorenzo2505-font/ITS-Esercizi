m: dict= {"key1" :  "valore1"}
print(m)
m: dict = {"key1" : {"key1" : "valore1"}} #un dizionario può avere altri dizionari (annidati)
print(m)
m: dict= {"key1" :  5}
print(m)
m: dict = {}
m["key"]=1
print(m)
m["key2"]= [1, 2, 3] #lista
print(m) 




#Dichiariazione del dizionario 
l: dict={"a" : 1, "b" :  2, "c" : 3}
#aggiunta elemento
l["d"]=4
print(l)
variabile: int = l["a"]
print(f"il valore di {variabile=}") 
#con f e le graffe e l'uguale faccio vedere in output che il valore della variabile è 1


c: dict = {"i" : 1, "j" :  2, "k" : 3}
l["inner"]= c #abbiamo messo il dizionario c in l associandolo a inner(no specifica, qualsiasi nome)
l["inner"] ["k"] #con il dizionario l associato ad inner si vuole accedere a k 

#esmpio

menu: dict = {"menu_estivo": {"Pizza" : 15, "Pasta" : 10, "insalata" : 5}}
#abbiamo dichiarato il menu con all'interno un altro menu estivo annidato

menu ["menu_estivo"] ["Pasta"]

menu_invernale: dict = {"Pizza" : 20, "Pasta" : 15, "Insalata" : 10}
#dichiariamo il menu invernale 
menu["menu_invernale"] = menu_invernale
#insieriamo il menu invernale nel menu
print (menu) #fa vedere tutto 
menu["menu_estivo"] ["Bistecca"]=25 #inserisco la bistecca nel menu estivo
menu["menu_invernale"] ["Bistecca"]=30
prezzo=menu["menu_estivo"].pop("Pizza") 
#viene rimossa dal menu estivo la pizza e il prezzo ma salvandolo ci si può far comunque restituire il valore
print(menu)
print(f"{prezzo=}")
menu["menu_estivo"] ["Pizza"] = 150 #modifico il prezzo
menu ["menu_invernale"]  ["Pasta"]=42
