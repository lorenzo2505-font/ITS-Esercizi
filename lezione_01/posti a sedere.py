posti = 20
occupati = 0
option: str = None



while (option != "esci"):
  option = str(input("inserisci opzione: "))
  if (option != "prenota") and (option != "libera") and (option != "visualizza"):
    print("errore")
  else:
    if option == "prenota":
            occupati+=1
            posti-=1
    if option == "libera":
            posti+=1
            occupati-=1
    if option == "visualizza":
            print(f"ci sono {occupati} posti occupati")
            print(f"ci sono {posti} posti liberi")
