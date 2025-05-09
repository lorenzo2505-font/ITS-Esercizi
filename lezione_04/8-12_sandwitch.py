'''8-12. Sandwich: scrivi una funzione che accetti un elenco di elementi che una persona desidera in un sandwich.
 La funzione dovrebbe avere un parametro che raccolga tutti gli elementi forniti dalla chiamata di funzione e 
 dovrebbe stampare un riepilogo del sandwich ordinato.
   Chiama la funzione tre volte, utilizzando ogni volta un numero diverso di argomenti.'''

def ingredienti (*args):
    mylist: list = []
    for i in args:
        mylist.append(i)
    print(mylist)

ingredienti("salame")
ingredienti("prosciutto", "cheddar")
ingredienti ("capocollo", "maionese", "sottiletta lite")