Menu: dict= {"Pasta" : 10.50, "Pizza" : 9.0, "Insalata" :  6.5, "Vino" :  4.0,  "Acqua" : 2.30 }
prezzo_pasta= Menu["Pasta"]
prezzo_vino= Menu["Vino"] 
print(prezzo_pasta)
print(prezzo_vino)
Menu["Caffe'"]=3.50 #aggiunta una nuova chiave e valore al dizionario 
print(Menu)
Menu.pop("Insalata")
print(Menu)
Menu["Pizza"]=8.0
print(Menu)

