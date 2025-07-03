
name_list: list[str] = []

ripetizioni: list = []

distinti = 0

while True:

    nome: str = str(input("inserisce nome: "))

    if not(nome) or len(nome) >= 20:

        raise ValueError("inserire un nome non vuoto e con meno di 20 caratteri")
    
    if nome in name_list:

        ripetizioni.append(nome)



        break

    else:

        name_list.append(nome)


    if len(name_list) == 30:
        break

    
    




l_max = 0

parola_max = None




for i in name_list:

    if len(i) > l_max:

        l_max = len(i)

        parola_max = i 




print(f"hai inserito in totale {len(name_list) + len(ripetizioni)} nomi")


print(f"hai inserito {len(name_list)} nomi distinti")

print(f"la parola più lunga è: {parola_max} con una lunghezza di {l_max}")










    

    

    





    

    