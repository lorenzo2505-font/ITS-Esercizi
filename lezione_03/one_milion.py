'''4-4. Un milione: crea un elenco dei numeri da uno a un milione, quindi utilizza un ciclo for per stampare i numeri. 
(Se l'output impiega troppo tempo, interrompilo premendo CTRL-C o chiudendo la finestra di output.)'''

mylist: list[int] = []
for i  in range(1, 1000000 + 1):
    mylist.append(i)
    print(mylist)