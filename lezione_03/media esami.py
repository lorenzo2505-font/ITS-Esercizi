'''Progettare un algoritmo che consenta di inserire all'utente un elenco di voti non negativi relativi ad un esame, calcolandone la media.
 L'algoritmo deve chiedere all'utente se vuole inserire un voto. 

Se la risposta è "SI", allora l'utente può procedere ad inserire il voto. 
L'algoritmo deve consentire all'utente di inserire voti fin quando la risposta dell'utente sarà "NO". 

Infine, mostrare in output il valore medio dei voti inseriti.'''

somma = 0
i = 0
option: str = None
while True:
    option = str(input("vuoi inserire un voto ? : "))
    if option == "no":
        break
    if (option != "si") and (option != "no"):
        print("errore")
    else:
        if option == "si":
            voto = int(input("inserisci voto: "))
            i+=1
            somma = somma + voto
            media = somma / i
print(media)
